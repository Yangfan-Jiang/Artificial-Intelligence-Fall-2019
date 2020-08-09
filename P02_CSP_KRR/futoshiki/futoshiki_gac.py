import copy


'''
load data
'''

def load_data(case):
    inequalities = []
    cell=[]
    with open("test" + str(case) + ".txt") as file:
        # read data into memory
        data = file.readlines()
        # get size of blocks (n * n)
        n = int(data[0])
        
        # initialize the variable domain and constraint of each posotion 
        init_domain = [item for item in range(1, n+1)]
        var_domain = {}
        constraint = {}
        for i in range(n):
            for j in range(n):
                var_domain[(i, j)] = init_domain[:]
                constraint[(i, j)] = []

        '''
        set all diff
        '''
        for pos in constraint.keys():
            row = ( (pos[0], i) for i in range(n) )
            column = ( (i, pos[1]) for i in range(n) )
            rowDif = (row, 'AllDif')
            columnDif = (column, 'AllDif')
            constraint[pos].append(rowDif)
            constraint[pos].append(columnDif)
        
        # load bigger/smaller constraints
        # always save inequalities with 'bigger' form
        for i in range(1,len(data)):
            for j in range(len(data[i])):
                pos = ()
                pos1 = ()
                pos2 = ()
                bigger = ()
                # odd row save the value of each cell
                if i % 2 == 1:
                    pos = ((i-1)//2, j//2)
                    # left position of cell
                    pos1 = (pos[0], (j-1)//2)
                    # right position of cell
                    pos2 = (pos[0], pos1[1]+1)
                else:
                    # upper position of cell
                    pos1 = ((i-2)//2, j//2)
                    # down position of cell
                    pos2 = (pos1[0]+1, j//2)
                    
                if data[i][j].isdigit():
                    # DO NOT change the initial value of each cell
                    var_domain[pos] = [int(data[i][j])]
                    cell.append(pos)
                elif data[i][j] in ('<','^'):
                    bigger = (pos2,pos1)
                elif data[i][j] in ('>','V'):
                    bigger = (pos1,pos2)
                    
                if bigger:
                    inequalities.append(bigger)
                    curr_constraints=(inequalities[-1], 'bigger')
                    constraint[pos1].append(curr_constraints)
                    constraint[pos2].append(curr_constraints)
    return var_domain, constraint, cell, n, inequalities



'''
implementation of forward checking
'''
# check inequalities
def check_inequ(var, var_domain, inequalities, unassigned):
    pos, value = var
    for inequality in inequalities:
        i, j = inequality
        # smaller
        if pos == i and j in unassigned:
            new_domain = []
            for item in var_domain[j]:
                if item < value:
                    new_domain.append(item)
                    
            var_domain[j] = new_domain[:]
            if not var_domain[j]:
                return False
            
        # bigger
        elif pos == j and i in unassigned:
            new_domain = []
            for item in var_domain[i]:
                if item > value:
                    new_domain.append(item)
            var_domain[i] = new_domain[:]
            if not var_domain[i]:
                return False
    return True


# check different value for same row and column
def check_diff_constrain(var, var_domain, unassigned, size):
    pos, value = var
    # check row
    row = pos[0]
    col = pos[1]
    for i in range(size):
        if i == col:
            continue
        if not (row,i) in unassigned:
            continue
            
        if value in var_domain[(row,i)]:
            var_domain[(row,i)].remove(value)
        if not var_domain[(row,i)]:
            return False
            
    # check column
    for i in range(size):
        if i == row:
            continue
        if not (i,col) in unassigned:
            continue
            
        if value in var_domain[(i,col)]:
            var_domain[(i,col)].remove(value)
        if not var_domain[(i,col)]:
            return False
    return True


# check if variables satisfy inequalities
def satisfy_inequ(var_domain,inequalities):
    for inequality in inequalities:
        pos1,pos2 = inequality
        domain1 = var_domain[pos1]
        domain2 = var_domain[pos2]
        
        if max(domain1) <= min(domain2):
            return False
        
        # change the domain of variables
        tmp_domain = []
        for i in domain1:
            if i > min(domain2):
                tmp_domain.append(i)
        var_domain[pos1] = tmp_domain[:]
        
        tmp_domain = []
        for i in domain2:
            if i < max(domain1):
                tmp_domain.append(i)
        var_domain[pos2] = tmp_domain[:]
    return True

# Forward Checking
def FC(var, var_domain, inequalities, unassigned, size):
    if not check_diff_constrain(var, var_domain, unassigned, size):
        return False
    if not check_inequ(var, var_domain, inequalities, unassigned):
        return False
    if not satisfy_inequ(var_domain, inequalities):
        return False
    return True


# push constraint to GAC_Queue
def push_constraint(pos):
    for c in constraint[pos]:
        if c not in GAC_Queue:
            GAC_Queue.append(c)
    
    
# variables satisfy diff_constrain
def satisfy_diff_constrain(diff_constrain):
    for i in diff_constrain:
        for j in range(len(var_domain[i])-1, -1, -1):
            val = var_domain[i][j]
            for k in diff_constrain:
                if k != i and len(var_domain[k])==1:
                    if var_domain[k] == val:
                        var_domain[i].pop(j)
                        if not var_domain[i]:
                            return False
                        push_constraint(i)
    return True
    
# GAC_Enforce
def GAC_Enforce(GAC_Queue,var_domain,unassigned,constraint):
        
    # check satisfy inequalities
    def satisfy_inequ_GAC(inequality):
        pos1, pos2 = inequality
        if not var_domain[pos1] or not var_domain[pos2]:
            return False
        domain1 = var_domain[pos1]
        domain2 = var_domain[pos2]
        size1 = len(domain1)
        size2 = len(domain2)
        var_domain[pos1] = [i for i in domain1 if i > min(domain2)]
        var_domain[pos2] = [i for i in domain2 if i < max(domain1)]
        if not var_domain[pos1] or not var_domain[pos2]:
            return False
        if size1 > len(var_domain[pos1]):
            push_constraint(pos1)
        if size2 > len(var_domain[pos2]):
            push_constraint(pos2)
        return True

    while GAC_Queue:
        c = GAC_Queue.pop(0)
        # DWO occurs
        if not satisfy_diff_constrain(c[0]) or (c[1] == 'bigger' and not satisfy_inequ_GAC(c[0])) :
            GAC_Queue = None
            return False
    return True


def GAC(var_domain,inequalities,unassigned,constraint,size):
    # all value has been assigned (find a solution)
    if not unassigned:
        return var_domain
        
    # using MRV
    # find the min unassigned domain
    unassigned_size = list(map(lambda x:len(var_domain[x]), unassigned))
    min_ele = min(unassigned_size)
    index = unassigned_size.index(min_ele)
    v = unassigned.pop(index)
    
    tmp_domain = copy.deepcopy(var_domain)
    for d in tmp_domain[v]:
        var_domain[v] = [d]
        GAC_Queue = constraint[v]
        # using both FC and GAC
        flag = FC((v,d),var_domain,inequalities,unassigned,size)
        if flag and GAC_Enforce(GAC_Queue, var_domain, unassigned, constraint):
            # return solution
            solution = GAC(var_domain, inequalities, unassigned, constraint, size)
            if solution:
                return solution
        #restore
        var_domain = copy.deepcopy(tmp_domain)
    unassigned.append(v)
    return False

#print graph
def print_ans(var_domain, size):
    for key, value in var_domain.items():
        print(value, end=' ')
        if key[1] == size-1:
            print()


# init cells
def init_cell(var_domain, cell, inequalities, unassigned, size):
    for i in cell:
        check_diff_constrain((i,var_domain[i][0]),var_domain,unassigned,size)
        check_inequ((i,var_domain[i][0]),var_domain,inequalities,unassigned)
    flag = True
    while flag:
        flag = False
        satisfy_inequ(var_domain, inequalities)
        for pos in unassigned:
            # if an unassigned value has only one domain
            if len(var_domain[pos]) == 1:
                flag = True
                check_diff_constrain((pos, var_domain[pos][0]), var_domain, unassigned, size)
                check_inequ((pos, var_domain[pos][0]), var_domain, inequalities, unassigned)
                unassigned.remove(pos)

if __name__ == '__main__':
    # test totally 5 cases
    for case in range(1,6):
        print('case #'+str(case))
        var_domain, constraint, cell, size, inequalities = load_data(case)
        unassigned = [i for i in var_domain.keys() if len(var_domain[i])>1]
        init_cell(var_domain, cell, inequalities, unassigned, size)
        res = GAC(var_domain, inequalities, unassigned, constraint, size)
        if res:
            print('run successfully')
            print_ans(res, size)
        else: 
            print('no solution!')
        print()
