import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'date2': np.random.randn(5)})

for name, group in df.groupby('key1'):
    print(name)
    print(group, '\n')

print('xxxxxx\n')

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group, '\n')

# 如何选择某一个分组出来单独进行操作
pieces = dict(list(df.groupby('key1')))
print(pieces['b'], '\n')

# 列维度进行分组
print(df.dtypes, '\n')

grouped = df.groupby(df.dtypes, axis=1)
for dtype, group in grouped:
    print(dtype, '\n', group, '\n')