import pandas as pd
from pandas.tseries.offsets import Hour, Minute


# 频率和日期偏置
hour = Hour()
print(hour)

four_hours = Hour(4)
print(four_hours)

print(pd.date_range('2000-01-01', '2001-01-03 23:59', freq='4h'), '\n')

print(Hour(2) + Minute(30), '\n')

print(pd.date_range('2000-01-01', periods=10, freq='1h30min'), '\n')

# 月中某星期的日期
# WOM: week of month，月中某星期
# 每月第3个星期5
rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')
print(rng, '\n')