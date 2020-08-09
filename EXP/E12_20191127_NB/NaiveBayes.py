from load_data import load_data
import pandas as pd
import numpy as np


label = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital−status', 
        'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
        'hours_per_week', 'native_country', 'classfication']
        
numeric = ['age', 'fnlwgt', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']

#print(df[27:30])

def Guassian_Distribution(df):
    '''
    fitting Guassian Distribution
    calculate the mean and variance value of continuous data
    
    Return: dict {'label':[sigma**2, mu]}
    '''
    parameters_y = {}       # parameters of guassian distribution
    parameters_not_y = {}
    for l in numeric:
        parameters_y[l] = [ df[df.classfication=='>50K'][l].var(), df[df.classfication=='>50K'][l].mean()]
        parameters_not_y[l] = [ df[df.classfication=='<=50K'][l].var(), df[df.classfication=='<=50K'][l].mean()]
    return parameters_y, parameters_not_y

def Guassian(label, xi, yk, py, pnoty):
    '''
    calculate the probability of Guassian Distribution
    P(x=xi|y=yk)
    '''
    if yk == '>50K':
        var = py[label][0]
        mu = py[label][1]
    else:
        var = pnoty[label][0]
        mu = pnoty[label][1]
    return ( 1 / (np.sqrt(2*np.pi*var)) ) * np.exp(- (xi-mu)**2/(2*var))

def generate_prob(py, pnoty):
    '''
    generate P(xi|y)
    Return: dict {'y': {('label','xi'):P(xi|y)}
                  'not y':{('label','xi'):P(xi|-y)} } 
    '''
    dict = {}
    dict['>50K'] = {}
    dict['<=50K'] = {}
    for l in label[:-1]:
        values = np.unique(df[l].values)
        if l in numeric:
            continue
        for v in values:
            dict['>50K'][(l, v)] = df[(df.classfication=='>50K') & (df[l]==v)].count()[0] / \
                      df[df.classfication=='>50K'].count()[0]
            dict['<=50K'][(l, v)] = df[(df.classfication=='<=50K') & (df[l]==v)].count()[0] / \
                      df[df.classfication=='<=50K'].count()[0]
    return dict

def argmax_y(x, P_t, P_f, py, pnoty, p_dict):
    '''
    Input: x, y
    x: dict ['label':x_1, 'label':x_2, ..., 'label':x_n]
    y: boolean the classfication
    
    Return: argmax_y P(y)*{P(x_i|y)}
    '''
    multiply_y = 1        # >50K
    multiply_not_y = 1    # <=50K
    for key, value in x.items():
        # calculate P(x_i|y)
        if key in numeric:
            multiply_y *= Guassian(key, value, '>50K', py, pnoty)
            multiply_not_y *= Guassian(key, value, '<=50K', py, pnoty)
            continue
        multiply_y *= p_dict['>50K'][(key, value)]
        multiply_not_y *= p_dict['<=50K'][(key, value)]
    
    if P_t*multiply_y > P_f*multiply_not_y:
        return '>50K'
    return '<=50K'

if __name__ == '__main__':
    # take >50K True, <50K False
    # calculate P(y) and P(-y)
    
    data, df = load_data(r'adult.data')
    P_t = df[df.classfication=='>50K'].count()[0]/len(df)
    P_f = 1-P_t
    
    parameters_y, parameters_not_y = Guassian_Distribution(df)
    p_dict = generate_prob(parameters_y, parameters_not_y)
    test_data, test_df = load_data(r'adult.test')
    
    s = 0
    for i in test_data:
        ans = i['classfication']
        
        del(i['classfication'])
        prediction = argmax_y(i, P_t, P_f, parameters_y, parameters_not_y, p_dict)
        
        if prediction == ans:
            s += 1
    print('Accuracy:', s/len(test_data))
    

'''
print('>50K')
for k,v in parameters_y.items():
    print(k ,v)

print('-------\n<50K')
for k,v in parameters_not_y.items():
    print(k ,v)
#print(len(df))
#print(P_t)
'''

