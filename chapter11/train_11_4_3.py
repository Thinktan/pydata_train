import pandas as pd
import numpy as np

# 不同时区的操作
rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
print()
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts = pd.Series(list(range(0, len(rng))), index=rng)
print(ts, '\n')

ts1 = ts[:7].tz_localize('Europe/London')
ts2 = ts1[2:].tz_convert('Europe/Moscow')
print(ts1)
print(ts1.index, '\n')
print(ts2, '\n')
print(ts2.index, '\n')

result = ts1+ts2
print(result)
print(result.index, '\n')