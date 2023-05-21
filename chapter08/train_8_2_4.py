
import pandas as pd
import numpy as np

a = pd.Series([np.nan, 2.5, 0.0, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series([0.0, np.nan, 2., np.nan, np.nan, 5.],
              index=['a', 'b', 'c', 'd', 'e', 'f'])

print(np.where(pd.isnull(a), b, a), '\n')

print(b.combine_first(a), '\n') # 根据索引来找填充值

# combine_first in DataFrame
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                    'b': [np.nan, 2., np.nan, 6.],
                    'c': range(2, 18, 4)})

df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                    'b': [np.nan, 3., 4., 6., 8.]})

print(df1, '\n')
print(df2, '\n')
print(df1.combine_first(df2), '\n')


a = pd.Series([np.nan, 2.5, 0.0, 3.5, 4.5, np.nan, 5.5],
              index=['f', 'e', 'd', 'c', 'b', 'a', 'h'])

b = pd.Series([0.0, np.nan, 2., np.nan, np.nan, 5., 6.],
              index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(b.combine_first(a), '\n') # 根据索引来找填充值