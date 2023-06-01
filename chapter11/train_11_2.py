import pandas as pd

s1 = pd.Series([11, 22, 33, 44], index=[1, 2, 3, 4])
s2 = pd.Series([22, 44], index=[2, 4])

# print(s1)
# print(s2)
# print(s1+s2)


from datetime import datetime
import numpy as np

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)
print(ts, '\n')

print(ts.index, '\n')

print(ts + ts[::2], '\n')

# pandas使用NumPy的datetime64数据类型在纳秒级的分辨率下存储时间戳
print(ts.index.dtype, '\n')

# DatetimeIndex中的标量值是pandas的Timestamp对象
stamp = ts.index[0]
print(type(stamp), '\n')

