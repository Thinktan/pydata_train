import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'date1': np.random.randn(5),
                   'date2': np.random.randn(5)})

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print(k1, k2)
    print(group, '\n')

print('----------------------')

for (k1, k2), group in df.groupby(['key1', 'key2'])['date2']:
    print(k1, k2)
    print(group, '\n')

print('----------------------')

print(df.groupby(['key1', 'key2'])[['date2']].sum(), '\n')
print('----------------------')


# 如果传递的是列表或数组，则此索引操作返回的对象是分组的DataFrame；
# 如果只有单个列名作为标量传递，则为分组的Series
print(df.groupby(['key1', 'key2'])['date2'])
print(df.groupby(['key1', 'key2'])[['date2']])
print(df.groupby(['key1', 'key2'])[['date1', 'date2']])
print(df.groupby('key1')) #DataFrameGroupBy
print(df.groupby('key1')['date1']) #SeriesGroupBy
print(df.groupby('key1')[['date1', 'date2']])
print('xxx  ', df.groupby('key1')['date1', 'date2'])
# print('----------------------')
# for k1, group in df.groupby(['key1']):
#     print(k1)
#     print(group, '\n')

# print('----------------------')
#
# for k1, group in df.groupby(['key1'])['date2']:
#     print(k1)
#     print(group, '\n')
#
# print('----------------------')
#
# for k1, group in df.groupby(['key1'])[['date2']]:
#     print(k1)
#     print(group, '\n')