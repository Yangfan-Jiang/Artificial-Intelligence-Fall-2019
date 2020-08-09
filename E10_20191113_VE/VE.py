class VariableElimination:
    @staticmethod
    def inference(factorList, queryVariables, 
    orderedListOfHiddenVariables, evidenceList):
        for ev in evidenceList.keys():
            delete_list = []
            add_list = []
            for factor in factorList:
                if ev in factor.varList:
                    temp_factor = factor.restrict(ev, evidenceList[ev])
                    delete_list.append(factor)
                    if temp_factor:
                        add_list.append(temp_factor)
            for ele in delete_list:
                factorList.remove(ele)
            factorList += add_list

        for var in orderedListOfHiddenVariables:
            z_list = [i for i in factorList if var in i.varList]
            z_len = len(z_list)
            tmp_node = z_list[0]
            for i in range(1, z_len):
                tmp_node = tmp_node.multiply(z_list[i])
            
            tmp_node = tmp_node.sumout(var)
            factorList.append(tmp_node)
            for i in z_list:
                factorList.remove(i)
            
            
        #print("RESULT:")
        res = factorList[0]
        for factor in factorList[1:]:
            res = res.multiply(factor)
        total = sum(res.cpt.values())
        res.cpt = {k: v/total for k, v in res.cpt.items()}

        #print(res.cpt)
        return res
        #res.printInf()
        
    @staticmethod
    def printFactors(factorList):
        for factor in factorList:
            factor.printInf()

class Util:
    @staticmethod
    def to_binary(num, len):
        return format(num, '0' + str(len) + 'b')

class Node:
    def __init__(self, name, var_list):
        self.name = name
        self.varList = var_list
        self.cpt = {}
        
    def setCpt(self, cpt):
        self.cpt = cpt
        
    def printInf(self):
        print("Name = " + self.name)
        print(" vars " + str(self.varList))
        for key in self.cpt:
            print("   key: " + key + " val : " + str(self.cpt[key]))
        print("")

    def multiply(self, factor):
        """function that multiplies with another factor"""
        # factor: a Node instance
        # find the in common variables, generate new variable list and cpt
        in_common = [i for i in self.varList if i in factor.varList]
        self_varlist_remain = [i for i in self.varList if i not in in_common]
        factor_varlist_remain = [i for i in factor.varList if i not in in_common]
        
        newList = self_varlist_remain[:]
        newList += factor_varlist_remain
        newList += in_common
        
        self_incommon_index = [self.varList.index(i) for i in in_common]
        factor_incommon_index = [factor.varList.index(i) for i in in_common]
        
        new_list_len = len(newList)
        self_list_len = len(self_varlist_remain)
        factor_list_len = len(factor_varlist_remain)
        
        # generate new cpt
        new_cpt = {}
        for i in range(0, 2**new_list_len):
            key = Util.to_binary(i, new_list_len)
            '''
            map: key ==> self(factor).cpt
            '''
            # self list
            self_cpt_key = ['-1' for i in range(len(self.varList))]
            factor_cpt_key = ['-1' for i in range(len(factor.varList))]
            for index in range(len(self_incommon_index)):
                self_cpt_key[self_incommon_index[index]] = str(key[self_list_len + factor_list_len + index])
            
            index = 0
            for i in range(len(self_cpt_key)):
                if self_cpt_key[i] == '-1':
                    self_cpt_key[i] = key[index]
                    index += 1
            self_cpt_key = "".join(self_cpt_key)
                        
            # factor list
            for index in range(len(factor_incommon_index)):
                factor_cpt_key[factor_incommon_index[index]] = str(key[self_list_len + factor_list_len + index])
            
            index = self_list_len
            for i in range(len(factor_cpt_key)):
                if factor_cpt_key[i] == '-1':
                    factor_cpt_key[i] = key[index]
                    index += 1
            factor_cpt_key = "".join(factor_cpt_key)
            new_cpt[key] = self.cpt[self_cpt_key] * factor.cpt[factor_cpt_key]
                
        new_node = Node("f" + str(newList), newList)
        new_node.setCpt(new_cpt)
        return new_node

    def sumout(self, variable):
        """function that sums out a variable given a factor"""
        new_var_list = self.varList[:]
        new_var_list.remove(variable)
        
        index = self.varList.index(variable)
        var_len = len(self.varList)
        
        tmp_cpt = self.cpt.copy()
        new_cpt = {}

        while tmp_cpt:
            key = list(tmp_cpt.keys())[0]
            key_list = list(key)
            del(key_list[index])
            key_list = ''.join(key_list)
            key2 = list(key)
            
            if key2[index] == '0':
                key2[index] = '1'
            else:
                key2[index] = '0'
            
            key2 = ''.join(key2)
            new_cpt[key_list] = tmp_cpt[key] + tmp_cpt[key2]
            del(tmp_cpt[key])
            del(tmp_cpt[key2])
            
        new_node = Node("f" + str(new_var_list), new_var_list)
        new_node.setCpt(new_cpt)
        return new_node

    def restrict(self, variable, value):
        """function that restricts a variable to some value 
        in a given factor"""
        new_var_list = self.varList[:]
        new_var_list.remove(variable)
        
        index = self.varList.index(variable)
        l = len(self.varList)
        
        new_key = list(self.cpt.keys())
        del_key = []
        
        for i in new_key:
            if i[index] != value:
                del_key.append(i)

        for i in del_key:
            new_key.remove(i)
        
        new_cpt = {}

        new_key = [i[:index]+i[index+1:] for i in new_key]
        
        for i in new_key:
            key2 = list(i)
            key2.insert(index, value)
            key2 = ''.join(key2)
            new_cpt[i] = self.cpt[key2]
        
        new_node = Node("f" + str(new_var_list), new_var_list)
        new_node.setCpt(new_cpt)
        #print(new_cpt)
        if l == 1:
            return None
        return new_node
        
# create nodes for Bayes Net
B = Node("B", ["B"])
E = Node("E", ["E"])
A = Node("A", ["A", "B","E"])
J = Node("J", ["J", "A"])
M = Node("M", ["M", "A"])

# Generate cpt for each node
B.setCpt({'0': 0.999, '1': 0.001})
E.setCpt({'0': 0.998, '1': 0.002})
A.setCpt({'111': 0.95, '011': 0.05, '110':0.94,'010':0.06,
'101':0.29,'001':0.71,'100':0.001,'000':0.999})
J.setCpt({'11': 0.9, '01': 0.1, '10': 0.05, '00': 0.95})
M.setCpt({'11': 0.7, '01': 0.3, '10': 0.01, '00': 0.99})


res = VariableElimination.inference([B,E,A,J,M], ['A'], ['B', 'E', 'J', 'M'], {})
print('P(Alarm) =', res.cpt['1'])
res = VariableElimination.inference([B,E,A,J,M], ['J','M'], ['B','E','A'], {})
print('P(J&&~M) =', res.cpt['10'])
res = VariableElimination.inference([B,E,A,J,M], ['A'], ['B','E'], {'J':'1', 'M':'0'})
print('P(A |J&&~M) =', res.cpt['1'])
res = VariableElimination.inference([B,E,A,J,M], ['B'], ['E', 'J', 'M'], {'A':'1'})
print('P(B |A) =', res.cpt['1'])
res = VariableElimination.inference([B,E,A,J,M], ['B'], ['E', 'A'], {'J':'1', 'M':'0'})
print('P(B |J&&~M) =', res.cpt['1'])
res = VariableElimination.inference([B,E,A,J,M], ['J', 'M'], ['E', 'A'], {'B':'0'})
print('P(J&&~M |B) =', res.cpt['10'])

