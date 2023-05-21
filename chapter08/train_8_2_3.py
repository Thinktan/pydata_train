

import numpy as np
import pandas as pd

arr = np.arange(12).reshape((3, 4))
print(arr, '\n')

print(np.concatenate([arr, arr], axis=1), '\n')

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

print(pd.concat([s1, s2, s3]), '\n')


s4 = pd.concat([s1, s3])
print(s4, '\n')
print(pd.concat([s1, s4], axis=1), '\n')
print(pd.concat([s1, s4], axis=1, join='inner'), '\n')

result = pd.concat([s1, s1, s3], keys=['one', 'one', 'three'])
print(result, '\n')

print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']), '\n')

# 扩展到DataFrame对象
df1 = pd.DataFrame(np.arange(6).reshape(3, 2),
                   index=['a', 'b', 'c'],
                   columns=['one', 'two'])

df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2),
                   index=['a', 'c'],
                   columns=['three', 'four'])

print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2'], names=['upper', 'lower']), '\n')

df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
print(pd.concat([df1, df2]), '\n')