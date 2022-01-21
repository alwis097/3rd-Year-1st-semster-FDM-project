


import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt



df=pd.read_csv('data/dateset_1.csv')
#df

# pre process
x = df.iloc[:,1:] # remove first column and get other all columns
x=x.replace('\/',' ',regex=True).astype(str) # remove "/"




items = set()
for col in x:
    items.update(df[col].unique())
#print(items)



itemset = set(items)

encoded_vals = []

for index, row in x.iterrows():
    rowset = set(row) 
    labels = {}
    uncommons = list(itemset - rowset)
    commons = list(itemset.intersection(rowset))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)
encoded_vals[0]
ohe_x = pd.DataFrame(encoded_vals)
#ohe_x

freq_items = apriori(ohe_x, min_support=0.01, use_colnames=True, verbose=1)
#freq_items

rules = association_rules(freq_items, metric="confidence", min_threshold=0.2)
#rules

antecedents_1 = rules["antecedents"].tolist()
antecedents_2=[list(x) for x in antecedents_1]
antecedents = [','.join(ele) for ele in antecedents_2]
#print(str(antecedents))

consequents_1 = rules["consequents"].tolist()
consequents_2=[list(x) for x in consequents_1]
consequents = [','.join(ele) for ele in consequents_2]
#print(str(consequents))

new_table = pd.DataFrame(
    {'antecedents': antecedents,
    'consequents': consequents,
    })
#new_table


d = new_table.groupby('antecedents')['consequents'].agg(list).to_dict()
print(d)


        
# def finder(key):
#     for d_key in d.keys():
#         if d_key == key:
            
#             item = d[d_key]
#             a = ",".join(str(x) for x in item)

#             print(a)
#             return a
#             break
#     else:
#         print("People also viewed these items:NONE\n")

# def finder(key):
#     search_item = key

#     for d_key in d.keys():
#         if d_key == search_item:
#         #print("People also viewed these items :")
#             item = d[d_key]
#             #print(item)
#             result = "\n".join(item[0:])
#             y=print(result)
#             x = "Freaquent Item(S) :"+y
#             return(x)
            
#             break
   

def finder(key):
    for d_key in d.keys():
        
        if d_key == key:
            #print(d_key)
            item = d[d_key]
            a = " , ".join(str(x) for x in item)
            print(a)
            x = "Frequent Item(s) :"+a
            return (x)
            break
           
    # else:
    #     print("People also viewed these items:NONE\n")
        


finder('root vegetables,other vegetables')




