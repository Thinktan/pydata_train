
import pandas as pd
import numpy as np
from datetime import datetime

dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])

dup_ts = pd.Series(np.arange(5), index=dates)
print(dup_ts, '\n')

print(dup_ts.is_unique, '\n')

print(dup_ts['1/3/2000'], '\n')
print(dup_ts['1/2/2000'], '\n')

newgrouped = dup_ts.groupby(level=0)
print(newgrouped)

for k, g in newgrouped:
    print(k)
    print('\\\\\\\\')
    print(g, '\n')

print(newgrouped.mean(), '\n')
print(newgrouped.count(), '\n')