import pandas as pd
import numpy as np

# 分组转换和"展开"GroupBy

df = pd.DataFrame({'key': ['a', 'b', 'c']*4,
                  'value': np.arange(12.)})
print(df, '\n')

g = df.groupby('key').value
print(g.mean(), '\n')

print(g.transform(lambda x: x.mean()), '\n')

print(g.transform(lambda x: x.rank(ascending=False)), '\n')

def normalize(x):
    return (x-x.mean())/x.std()

print(g.transform(normalize), '\n')

normalized = (df['value'] - g.transform('mean')) / g.transform('std')
print(normalized, '\n')