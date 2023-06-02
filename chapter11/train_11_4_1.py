import pytz
import pandas as pd
import numpy as np

# 时区的本地化和转换

print(pytz.common_timezones)
print(len(pytz.common_timezones))

tz = pytz.timezone('America/New_York')
print(tz)

rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts, '\n')

print(ts.index.tz, '\n')

# print(pd.date_range('3/9/2012 9:30', periods=6, freq='D', tz='UTC'))

ts_utc = ts.tz_localize('UTC')
print(ts_utc, '\n')
print(ts_utc.index, '\n')
print(ts_utc.tz_convert('America/New_York'), '\n')

ts_eastern = ts.tz_localize('America/New_York')
print(ts_eastern, '\n')
print(ts_eastern.tz_convert('UTC'), '\n')

print(type(ts))
print(type(ts.index))