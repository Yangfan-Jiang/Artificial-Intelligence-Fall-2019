import pandas as pd
import numpy as np

label = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital−status', 
        'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
        'hours_per_week', 'native_country', 'classfication']
        
numeric = ['age', 'fnlwgt', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']

# TODO: Construct the possible value of each labels and calculate the probability

def load_data(file_name):
    data = []
    with open(file_name) as f:
        sep = ', '
        for line in f:
            if len(line) < 2:
                continue
            if file_name[-1] == 't':
                if line[-2] != '.':
                    continue
            line = line.replace('\n','')
            line = line.replace('.','')
            line = line.split(sep)

            item = {}
            
            for index in range(len(label)):
                value = line[index]
                if label[index] in numeric and value != '?':
                    value = int(line[index])
                item[label[index]] = value
            data.append(item)
    df = pd.DataFrame(data)
    return data, df
    
def data_perprocess(data, df):
    # calculate the mean data and the max counts
    # replace missing data
    text_attr = [i for i in label if i not in numeric]
    
    replace_num = {}
    for i in numeric:
        replace_num[i] = df[i].mean()
        
    replace_text = {}
    for i in text_attr:
        replace_text[i] = df[i].value_counts().index[0]
    
    for item in data:
        for k in item.keys():
            if item[k] == '?' and k in numeric:
                item[k] = replace_num[k]
            elif item[k] == '?' and k in text_attr:
                item[k] = replace_text[k]        
    return data
    
def probability_table(df, label):
    '''
    calculate the probability of each attribute
    return type: dict
    format: {'label':{'attr1':p1, 'attr2', p2}, {'label2':...}}
    '''
    # initialize the data structure
    p_table = {}
    scale = {}
    for item in label:
        p_table[item] = {}
        scale[item] = {}
    
    '''
    age: 0-30, 31-40, 41-50, 51-60, >60
    fnlwgt: 0-100000, 100001-200000, 200001-300000, >300000
    education_num: 0-9, 10-13, >13
    capital_gain:0-5000, 5001-15000, 15001-30000, >30000
    capital_loss:0-500, 501-1000, 1001-2000, >2000
    hours_per_week:0-20, 21-35, 36-50, 51-65, >65
    '''
    total_num = len(df)
    
    # label that is not numeric
    text_attr = [i for i in label if i not in numeric]
    
    for attr in text_attr:
        # attribute types
        types = np.unique(df[attr].values)
        for t in types:
            p_table[attr][t] = \
                df[(df[attr]==t) & (df.classfication=='>50K')].count()[0] / df[df[attr]==t].count()[0]
            scale[attr][t] = df[df[attr]==t].count()[0] / total_num
    
    # age
    if 'age' in label:
        if df[df.age<=30].count()[0] != 0:
            p_table['age']['0-30'] = \
                df[(df.age<=30) & (df.classfication == '>50K')].count()[0] / df[df.age<=30].count()[0]
            scale['age']['0-30'] = df[df.age<=30].count()[0] / total_num
        if df[(df.age>=31) & (df.age<=40)].count()[0] != 0:
            p_table['age']['31-40'] = \
                df[(df.age>=31) & (df.age<=40) & (df.classfication=='>50K')].count()[0] / df[(df.age>=31) & (df.age<=40)].count()[0]
            scale['age']['31-40'] = df[(df.age>=31) & (df.age<=40)].count()[0] / total_num
        if df[(df.age>=41) & (df.age<=50)].count()[0] != 0:
            p_table['age']['41-50'] = \
                df[(df.age>=41) & (df.age<=50) & (df.classfication=='>50K')].count()[0] / df[(df.age>=41) & (df.age<=50)].count()[0]
            scale['age']['41-50'] = df[(df.age>=41) & (df.age<=50)].count()[0] / total_num
        if df[(df.age>=51) & (df.age<=60)].count()[0] != 0:
            p_table['age']['51-60'] = \
                df[(df.age>=51) & (df.age<=60) & (df.classfication=='>50K')].count()[0] / df[(df.age>=51) & (df.age<=60)].count()[0]
            scale['age']['51-60'] = df[(df.age>=51) & (df.age<=60)].count()[0] / total_num
        if df[df.age>=61].count()[0] != 0:
            p_table['age']['>60'] = \
                df[(df.age>=61) & (df.classfication=='>50K')].count()[0] / df[df.age>=61].count()[0]
            scale['age']['>60'] = df[df.age>=61].count()[0] / total_num

    # fnlwgt
    if 'fnlwgt' in label:
        if df[df.fnlwgt<=100000].count()[0] != 0:
            p_table['fnlwgt']['0-100000'] = \
                df[(df.fnlwgt<=100000) & (df.classfication == '>50K')].count()[0] / df[df.fnlwgt<=100000].count()[0]
            scale['fnlwgt']['0-100000'] = df[df.fnlwgt<=100000].count()[0] / total_num
        if df[(df.fnlwgt>=100001) & (df.fnlwgt<=200000)].count()[0] != 0:
            p_table['fnlwgt']['100001-200000'] = \
                df[(df.fnlwgt>=100001) & (df.fnlwgt<=200000) & (df.classfication == '>50K')].count()[0] / df[(df.fnlwgt>=100001) & (df.fnlwgt<=200000)].count()[0]
            scale['fnlwgt']['100001-200000'] = df[(df.fnlwgt>=100001) & (df.fnlwgt<=200000)].count()[0] / total_num
        if df[(df.fnlwgt>=200001) & (df.fnlwgt<=300000)].count()[0] != 0:
            p_table['fnlwgt']['200001-300000'] = \
                df[(df.fnlwgt>=200001) & (df.fnlwgt<=300000) & (df.classfication == '>50K')].count()[0] / df[(df.fnlwgt>=200001) & (df.fnlwgt<=300000)].count()[0]
            scale['fnlwgt']['200001-300000'] = df[(df.fnlwgt>=200001) & (df.fnlwgt<=300000)].count()[0] / total_num
        if df[df.fnlwgt>=300001].count()[0] != 0:
            p_table['fnlwgt']['>300001'] = \
                df[(df.fnlwgt>=300001) & (df.classfication == '>50K')].count()[0] / df[df.fnlwgt>=300001].count()[0]
            scale['fnlwgt']['>300001'] = df[df.fnlwgt>=300001].count()[0] / total_num

    # education_num
    if 'education_num' in label:
        if df[df.education_num<=9].count()[0] != 0:
            p_table['education_num']['0-9'] = \
                df[(df.education_num<=9) & (df.classfication == '>50K')].count()[0] / df[df.education_num<=9].count()[0]
            scale['education_num']['0-9'] = df[df.education_num<=9].count()[0] / total_num
        if df[(df.education_num>=10) & (df.education_num<=13)].count()[0] != 0:
            p_table['education_num']['10-13'] = \
                df[(df.education_num>=10) & (df.education_num<=13) & (df.classfication=='>50K')].count()[0] / df[(df.education_num>=10) & (df.education_num<=13)].count()[0]
            scale['education_num']['10-13'] = df[(df.education_num>=10) & (df.education_num<=13)].count()[0] / total_num
        if df[df.education_num>=14].count()[0]:
            p_table['education_num']['>13'] = \
                df[(df.education_num>=14) & (df.classfication=='>50K')].count()[0] / df[df.education_num>=14].count()[0]
            scale['education_num']['>13'] = df[df.education_num>=14].count()[0] / total_num

    # capital_gain
    if 'capital_gain' in label:
        if df[df.capital_gain<=5000].count()[0] != 0:
            p_table['capital_gain']['0-5000'] = \
                df[(df.capital_gain<=5000) & (df.classfication == '>50K')].count()[0] / df[df.capital_gain<=5000].count()[0]
            scale['capital_gain']['0-5000'] = df[df.capital_gain<=5000].count()[0] / total_num
        if df[(df.capital_gain>=5001) & (df.capital_gain<=15000)].count()[0] != 0:
            p_table['capital_gain']['5001-15000'] = \
                df[(df.capital_gain>=5001) & (df.capital_gain<=15000) & (df.classfication == '>50K')].count()[0] / df[(df.capital_gain>=5001) & (df.capital_gain<=15000)].count()[0]
            scale['capital_gain']['5001-15000'] = df[(df.capital_gain>=5001) & (df.capital_gain<=15000)].count()[0] / total_num
        if df[(df.capital_gain>=15001) & (df.capital_gain<=30000)].count()[0] != 0:
            p_table['capital_gain']['15001-30000'] = \
                df[(df.capital_gain>=15001) & (df.capital_gain<=30000) & (df.classfication == '>50K')].count()[0] / df[(df.capital_gain>=15001) & (df.capital_gain<=30000)].count()[0]
            scale['capital_gain']['15001-30000'] = df[(df.capital_gain>=15001) & (df.capital_gain<=30000)].count()[0] / total_num
        if df[df.capital_gain>=30001].count()[0] != 0:
            p_table['capital_gain']['>30000'] = \
                df[(df.capital_gain>=30001) & (df.classfication == '>50K')].count()[0] / df[df.capital_gain>=30001].count()[0]
            scale['capital_gain']['>30000'] = df[df.capital_gain>=30001].count()[0] / total_num

    # capital_loss
    if 'capital_loss' in label:
        if df[df.capital_loss<=500].count()[0] != 0:
            p_table['capital_loss']['0-500'] = \
                df[(df.capital_loss<=500) & (df.classfication == '>50K')].count()[0] / df[df.capital_loss<=500].count()[0]
            scale['capital_loss']['0-500'] = df[df.capital_loss<=500].count()[0] / total_num
        if df[(df.capital_loss>=501) & (df.capital_loss<=1000)].count()[0] != 0:
            p_table['capital_loss']['501-1000'] = \
                df[(df.capital_loss>=501) & (df.capital_loss<=1000) & (df.classfication == '>50K')].count()[0] / df[(df.capital_loss>=501) & (df.capital_loss<=1000)].count()[0]
            scale['capital_loss']['501-1000'] = df[(df.capital_loss>=501) & (df.capital_loss<=1000)].count()[0] / total_num
        if df[(df.capital_loss>=1001) & (df.capital_loss<=2000)].count()[0] != 0:
            p_table['capital_loss']['1001-2000'] = \
                df[(df.capital_loss>=1001) & (df.capital_loss<=2000) & (df.classfication == '>50K')].count()[0] / df[(df.capital_loss>=1001) & (df.capital_loss<=2000)].count()[0]
            scale['capital_loss']['1001-2000'] = df[(df.capital_loss>=1001) & (df.capital_loss<=2000)].count()[0] / total_num
        if df[df.capital_loss>=2001].count()[0] != 0:
            p_table['capital_loss']['>2000'] = \
                df[(df.capital_loss>=2001) & (df.classfication == '>50K')].count()[0] / df[df.capital_loss>=2001].count()[0]
            scale['capital_loss']['>2000'] = df[df.capital_loss>=2001].count()[0] / total_num

    # hours_per_week
    if 'hours_per_week' in label:
        if df[df.hours_per_week<=20].count()[0] != 0:
            p_table['hours_per_week']['0-20'] = \
                df[(df.hours_per_week<=20) & (df.classfication == '>50K')].count()[0] / df[df.hours_per_week<=20].count()[0]
            scale['hours_per_week']['0-20'] = df[df.hours_per_week<=20].count()[0] / total_num
        if df[(df.hours_per_week>=21) & (df.hours_per_week<=35)].count()[0] != 0:
            p_table['hours_per_week']['21-35'] = \
                df[(df.hours_per_week>=21) & (df.hours_per_week<=35) & (df.classfication == '>50K')].count()[0] / df[(df.hours_per_week>=21) & (df.hours_per_week<=35)].count()[0]
            scale['hours_per_week']['21-35'] = df[(df.hours_per_week>=21) & (df.hours_per_week<=35)].count()[0] / total_num
        if df[(df.hours_per_week>=36) & (df.hours_per_week<=50)].count()[0] != 0:
            p_table['hours_per_week']['36-50'] = \
                df[(df.hours_per_week>=36) & (df.hours_per_week<=50) & (df.classfication == '>50K')].count()[0] / df[(df.hours_per_week>=36) & (df.hours_per_week<=50)].count()[0]
            scale['hours_per_week']['36-50'] = df[(df.hours_per_week>=36) & (df.hours_per_week<=50)].count()[0] / total_num
        if df[(df.hours_per_week>=51) & (df.hours_per_week<=65)].count()[0] != 0:
            p_table['hours_per_week']['51-65'] = \
                df[(df.hours_per_week>=51) & (df.hours_per_week<=65) & (df.classfication == '>50K')].count()[0] / df[(df.hours_per_week>=51) & (df.hours_per_week<=65)].count()[0]
            scale['hours_per_week']['51-65'] = df[(df.hours_per_week>=51) & (df.hours_per_week<=65)].count()[0] / total_num
        if df[df.hours_per_week>=66].count()[0] != 0:
            p_table['hours_per_week']['>65'] = \
                df[(df.hours_per_week>=66) & (df.classfication == '>50K')].count()[0] / df[df.hours_per_week>=66].count()[0]
            scale['hours_per_week']['>65'] = df[df.hours_per_week>=66].count()[0] / total_num
    return p_table, scale
        
    
def Entropy(label, p_table, df, scale):
    '''
    calculate the entropy of label
    '''
    result = 0
    p = p_table[label]
    for attr in p:
        p1 = p[attr]
        p2 = 1 - p1
        if p1 == 0:
            term1 = 0
        else:
            term1 = p1*np.log2(p1)
        if p2 == 0:
            term2 = 0
        else:
            term2 = p2*np.log2(p2)
            
        result -= scale[label][attr]*(term1 + term2)
    return result
    
def select_attr(label, pt, df, scale):
    min = 9999
    attr = ''
    
    for i in label:
        if i == 'classfication':
            continue
        entropy = Entropy(i, pt, df, scale)
        if entropy < min:
            min = entropy
            attr = i
    return attr
    
def DecisionTreeLearning(train_data, attr, decision_tree, par_data):
    '''
    Take salary > 50k as positive example
    pt: probability_table
    '''
    # if train_data is empty, return plurality of parent examples
    if not train_data:
        decision_tree['result'] = par_data
        return
    # if all example have the same classfication
    flag = True
    for i in train_data:
        if i['classfication'] != train_data[0]['classfication']:
            flag = False
            break
    if flag:
        decision_tree['result'] = train_data[0]['classfication']
        return
    # if attribute is empty, return plurality of current data_set
    if not attr:
        df = pd.DataFrame(train_data)
        decision_tree['result'] = df['classfication'].value_counts().index[0]
        return
    
    df = pd.DataFrame(train_data)
    pt, scale = probability_table(df, attr)
    
    max_attr = select_attr(attr, pt, df, scale)

    attr_values = np.unique(df[max_attr].values)
    
    decision_tree[max_attr] = {}
    new_attr = attr[:]
    new_attr.remove(max_attr)
    
    plurality = df['classfication'].value_counts().index[0]
    decision_tree['plurality'] = plurality
    for value in attr_values:
        new_train_data = [i for i in train_data if i[max_attr]==value]
        decision_tree[max_attr][value] = {}
        DecisionTreeLearning(new_train_data, new_attr, decision_tree[max_attr][value], plurality)

def classify_validation(decision_tree, attr):
    if decision_tree.__contains__('result'):
        return decision_tree['result']
    for root, value in decision_tree.items():
        if value.__contains__(attr[root]):
            decision_tree = value[attr[root]]
            return classify_validation(decision_tree, attr)
        else:
            return decision_tree['plurality']

data, df = load_data(r'adult.data')
print(len(data))
data = data_perprocess(data, df)

decision_tree = {}
attr = label[:]
attr.remove('classfication')
DecisionTreeLearning(data, attr, decision_tree, '<=50K')

test_data, test_df = load_data(r'adult.test')
test_data = data_perprocess(test_data, test_df)
print(len(test_data))

s = 0
for i in test_data:
    ans = i['classfication']
    x = classify_validation(decision_tree, i)
    if x == ans:
        s+=1
print(s/len(test_data))