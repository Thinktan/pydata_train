import pandas as pd
import numpy as np

# 移位(前向和后向)日期
# Series和Dataframe中的shift方法会将整体数据前移或者后移，
# 而起索引保持原来位置不动，所以移动后索引所对应的数值会有所变化

ts = pd.Series(np.random.randn(4), index=pd.date_range('1/1/2000', periods=4, freq='M'))
print(ts, '\n')

# 移动数据，空位置使用np.nan填充
# print(ts.shift(2), '\n')
# print(ts.shift(-1), '\n')

# 指定freq参数后，移动的是索引，而不是数据
# print(ts.shift(2, freq='M'), '\n')

# 传递其他频率
print(ts.shift(3, freq='D'), '\n')
print(ts.shift(1, freq='90T'), '\n')


# a = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# b = pd.Series([2, 8, 24], index=['b', 'c', 'd'])
# print(b/a)
