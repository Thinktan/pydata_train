import json
import pandas as pd

db = json.load(open('../datasets/usda_food/database.json'))
print(len(db), '\n')

info_keys = ['description', 'group', 'id', 'manufacturer']
info = pd.DataFrame(db, columns=info_keys)
print(info[:5], '\n')
print(info.info(), '\n')
print(pd.value_counts(info.group)[:10], '\n')


# 营养素列表
nutrients = []

for rec in db:
    fnuts = pd.DataFrame(rec["nutrients"])
    fnuts["id"] = rec["id"]
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)
# print(nutrients.duplicated().sum())

nutrients = nutrients.drop_duplicates()
print(nutrients, '\n')

col_mapping = {'description': 'food', 'group': 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
print(info.info(), '\n')

col_mapping = {'description' : 'nutrient', 'group' : 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)
print(nutrients.info(), '\n')

ndata = pd.merge(nutrients, info, on='id', how='outer')
print(ndata.info(), '\n---------------\n')
print(ndata.iloc[30000], '\n')

import matplotlib.pyplot as plt

result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
result['Zinc, Zn'].sort_values().plot(kind='barh')
plt.show()








