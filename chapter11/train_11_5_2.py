
import pandas as pd
import numpy as np

# 季度区间频率
p = pd.Period('2012Q4', freq='Q-JAN')
print(p)
print(p.asfreq('D', 'start'))
print(p.asfreq('D', 'end'))
print('-------')
print(p.asfreq('B', 'e'))
print(p.asfreq('B', 'e')-1)
print((p.asfreq('B', 'e')-1).asfreq('T', 's'))
print('-------')

rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
ts = pd.Series(np.arange(len(rng)), index=rng)
print(ts)

print(rng.asfreq('B', 'e'))
print(rng.asfreq('B', 'e')-1)
print((rng.asfreq('B', 'e')-1).asfreq('T', 's'))
print((rng.asfreq('B', 'e')-1).asfreq('T', 's') + 16*60)
print(((rng.asfreq('B', 'e')-1).asfreq('T', 's') + 16*60).to_timestamp())