import pandas as pd
import numpy as np

# 向下采样
rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.arange(12), index=rng)

print(ts, '\n')
print(ts.resample('5min', closed='right').sum(), '\n')
print(ts.resample('5min', closed='right', label='right').sum(), '\n')
# print(ts.resample('5min', closed='right', label='right', loffset='-1s').sum(), '\n')
print(ts.resample('5min', closed='right', label='right').sum().shift(-1, freq='S'), '\n')

print(ts.resample('5min').sum(), '\n')

print(ts.resample('5min').ohlc(), '\n')