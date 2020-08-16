# AI Experiment #2: 15 puzzle problem
# 2019/9/8
__author__ = 'Yangfan Jiang (jiangyf29@mail2.sysu.edu.cn)'

'''
Solve 15 puzzle problem by Iterative Deepening A*
'''

from copy import *
import numpy as np

# 2 D list: 4*4
puzzle = []


def h(puzzle):
    '''
    The sum of the distances of the tiles from their goal positions
    
    Input:
    puzzle: 2 D list stand for current state of puzzle
    
    Returns:
    sum(int): the value of h function 
    '''
    sum = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if puzzle[i][j] != i*4+j+1 and puzzle[i][j] != 0:
                x = (puzzle[i][j]-1) // 4
                y = (puzzle[i][j]+3)%4
                sum += abs(x-i) + abs(y-j)
    return sum


def is_goal(puzzle):
    '''
    Judge whether the state is finish
    
    Input:
    puzzle: 2 D list stand for current state of puzzle
    
    Returns:
    Boolean value
    '''
    for i in range(0, 4):
        for j in range(0, 4):
            if puzzle[i][j] != i*4+j+1 and i*4+j+1!=16:
                return False
    return True


def successor(node):
    '''
    Find the successor of current state
    
    Input:
    node(2D list)
    
    Returns:
    next_states(list): neighbors of zero element
    '''
    index = 0
    curr_num = node[0][0]
    i = j = 0
    while curr_num != 0:
        index += 1
        i = index//4
        j = index%4
        curr_num = node[i][j]
    next_states = []
    next_pos = [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]
    for pos in next_pos:
        if 0<=pos[0]<=3 and 0<=pos[1]<=3:
            next = deepcopy(node)
            next[i][j] = next[pos[0]][pos[1]]
            next[pos[0]][pos[1]] = 0
            next_states.append(deepcopy(next))
    return next_states

def cost(node, succ):
    '''
    cost for search 1 step
    '''
    return 1

def is_inverse(root):
    '''
    Judeg whether the problem has a solution
    if the #inverse sequence pair of original state is odd
    there are definitely no solution
    
    Input:
    root(2D list): original state
    
    Output:
    0 or 1, repersent for whether there is a solution
    '''
    num_inverse = 0
    sequence = [i for item in root for i in item]
    l = len(sequence)
    for i in range(1, l):
        for j in range(0, i):
            if sequence[j] > sequence[i]:
                num_inverse += 1
    return (num_inverse%2) == 0

def ida_star(root):
    '''
    Implementtation of Iterative Deepening A*
    '''
    if is_inverse(root):
        print("No solution")
        return '','',''
    
    bound = h(root)
    path = [root]
    while True:
        t = search(path, 0, bound)
        if t == 'Found':
            return t, bound, path
        elif t == 'inf':
            return 'Not Found'
        bound = t
        print(t)

def search(path, g, bound):
    '''
    Deep First Search
    '''
    node = path[-1]
    f = g + h(node)
    if f > bound:
        return f
    if is_goal(node):    
        return 'Found'
        
    min = 1000000
    for succ in successor(node):
        if succ not in path:
            path.append(succ)
            t = search(path, g + cost(node, succ), bound)
            if t == 'Found':    
                return 'Found'
            if t < min:
                min = t
            path[:] = path[:-1]
    
    return min

def get_path(path):
    '''
    Transform sequence of states into sequence of steps
    each step is repersented by a number that needs to be moved
    '''
    trace = []
    l = len(path)
    for i in range(0, l-1):
        x = np.array(path[i])
        y = np.array(path[i+1])
        res = y - x
        pos = np.where(res > 0.1)
        pos_x = pos[0][0]
        pos_y = pos[1][0]
        trace.append(y[pos_x][pos_y])
    return trace

if __name__ == '__main__':
    t = [[1,6,2,3],[5,8,7,10],[9,12,0,4],[13,14,11,15]]
    x, y, z = ida_star(t)
    trace = get_path(z)
    print('----- solution -----')
    print(trace)

# ---- test cases ----
#t = [[0,5,15,14],[7,9,6,13],[1,2,12,10],[8,11,4,3]]
#t = [[6,10,3,15],[14,8,7,11],[5,1,0,2],[13,12,9,4]]
#t = [[1,3,6,4],[10,9,2,8],[0,5,7,12],[13,14,11,15]]
#t = [[1,2,4,8],[10,0,6,3],[5,9,7,11],[13,14,15,12]]
#t = [[1,2,8,3],[5,6,7,4],[9,0,10,12],[13,14,11,15]]
#t = [[12,5,2,4],[1,11,14,7],[8,13,0,10],[6,3,9,15]]
