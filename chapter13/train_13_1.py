import pandas as pd
import numpy as np

# pandas与建模代码的结合

data = pd.DataFrame({
    'x0': [1, 2, 3, 4, 5],
    'x1': [0.01, -0.01, 0.25, -4.1, 0.],
    'y': [-1.5, 0., 3.6, 1.3, -2.]})

print(data, '\n')
print(data.columns, '\n')
print(data.index, '\n')
print(data.values, '\n')

df2 = pd.DataFrame(data.values, columns=['one', 'two', 'three'])
print(df2, '\n')

df3 = data.copy()
df3['strings'] = ['a', 'b', 'c', 'd', 'e']
print(df3, '\n')
print(df3.values, '\n')

model_cols = ['x0', 'x1']
print(data.loc[:, model_cols].values, '\n')

data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'])
print(data, '\n')

dummies = pd.get_dummies(data.category, prefix='category')
print(dummies, '\n')
data_with_dummies = data.drop('category', axis=1).join(dummies)
print(data_with_dummies, '\n')

