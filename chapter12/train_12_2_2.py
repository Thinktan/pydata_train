import pandas as pd
import numpy as np

# 分组的时间重新采样
N = 15
times = pd.date_range('2017-05-20 00:00', freq='1min', periods=N)
df = pd.DataFrame({'time': times, 'value': np.arange(N)})
print(df, '\n')

print(df.set_index('time').resample('5min').count(), '\n')

df2 = pd.DataFrame({'time': times.repeat(3),
                    'key': np.tile(['a', 'b', 'c'], N),
                    'value': np.arange(N*3.)})

print(df2, '\n')

time_key = pd.Grouper(freq='5min')

df3 = df2.set_index('time')

resampled = (df3.groupby(['key', time_key]).sum())
print(resampled, '\n')
print(resampled.index, '\n')
print(resampled.reset_index(), '\n')