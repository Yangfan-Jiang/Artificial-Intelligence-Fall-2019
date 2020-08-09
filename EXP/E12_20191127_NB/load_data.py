import pandas as pd
import numpy as np

label = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital−status', 
        'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
        'hours_per_week', 'native_country', 'classfication']
        
numeric = ['age', 'fnlwgt', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']

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
    data = data_perprocess(data, pd.DataFrame(data))
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