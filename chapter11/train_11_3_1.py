
import pandas as pd
import numpy as np
from datetime import datetime

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)
print(ts, '\n')

resampler = ts.resample('D')
print(resampler)

# 生成日期范围
index = pd.date_range('2012-04-01', '2012-06-01')
print(index, '\n')

print(pd.date_range(start='2012-04-01', periods=20), '\n')

print(pd.date_range(end='2012-06-01', periods=20), '\n')

print(pd.date_range('2000-01-01', '2000-12-01', freq='BM'), '\n')
print('-----------------')
# 测试freq
print(pd.date_range('2000-01-01', '2000-02-01', freq='M'))
print('-----------------')


print(pd.date_range('2012-05-02 12:56:31', periods=5), '\n')

print(pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True), '\n')

