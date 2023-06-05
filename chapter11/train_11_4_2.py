import pandas as pd

# 时区感知时间戳对象的操作

stamp = pd.Timestamp('2011-03-12 04:00')
print(stamp.value)
stamp_utc = stamp.tz_localize('utc')
print(stamp_utc.value)
print(stamp_utc.tz_convert('America/New_York').value)

from pandas.tseries.offsets import Hour

stamp = pd.Timestamp('2012-03-12 01:30', tz='US/Eastern')
print(stamp)
print(stamp + Hour(), '\n')

stamp = pd.Timestamp('2012-11-04 00:30', tz='US/Eastern')
print(stamp)
print(stamp + 2*Hour())