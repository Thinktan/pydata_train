
import pandas as pd

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})

df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

# a b c
print(df1, '\n')
# a b d
print(df2, '\n')

# a b 交集
print(pd.merge(df1, df2, on='key'), '\n')

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})

df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})

print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'), '\n')

# outer join
print(pd.merge(df1, df2, on='key', how='outer'), '\n')

# left join
print(pd.merge(df1, df2, on='key', how='left'), '\n')

# right join
print(pd.merge(df1, df2, on='key', how='right'), '\n')

# case
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})

df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})

print(df1, '\n')
print(df2, '\n')

# 多对多连接是行的笛卡儿积
print(pd.merge(df1, df2, on='key', how='left'), '\n')
print(pd.merge(df1, df2, on='key', how='inner'), '\n')

# 使用多个键进行合并
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})

right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})

print(pd.merge(left, right, on=['key1', 'key2'], how='outer'), '\n')

print(pd.merge(left, right, on='key1'), '\n ')

print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')), '\n')