import pandas as pd
import numpy as np

# 将时间戳转换为区间

rng = pd.date_range('2000-01-01', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)
print(ts)

pts = ts.to_period() # 默认'D'
print(pts)

print('------------')

rng = pd.date_range('1/29/2000', periods=6, freq='D')
ts2 = pd.Series(np.random.randn(6), index=rng)
print(ts2)
print(ts2.to_period('M'))
print(ts2.to_period())
print(ts2.to_period().to_timestamp(how='end'))
# print(ts2.to_timestamp(how='end'))
print(type(ts2))
print(type(ts2.to_period()))