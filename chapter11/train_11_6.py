import pandas as pd
import numpy as np

# 重新采样与频率转换
# resample

rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts, '\n')
print(ts.resample('M'), '\n')
print(ts.resample('M').mean(), '\n')
print(ts.resample('M', kind='period').mean(), '\n')