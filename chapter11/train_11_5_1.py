import pandas as pd
import numpy as np

# 区间频率转换 PeriodIndex
p = pd.Period('2007', freq='A-DEC')
print(p)

print(p.asfreq('M', how='start'))
print(p.asfreq('M', how='end'), '\n')


p = pd.Period('2007', freq='A-JUN')
print(p)
print(p.asfreq('M', 'start'))
print(p.asfreq('M', 'end'), '\n')

p = pd.Period('Aug-2007', 'M')
print(p.asfreq('A-JUN'), '\n')

rng = pd.period_range('2006', '2009', freq='A-DEC')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts, '\n')

print(ts.asfreq('M', how='start'), '\n')
print(ts.asfreq('B', how='end'), '\n')
