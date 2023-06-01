from datetime import datetime
import numpy as np
import pandas as pd

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)
print(ts, '\n')

stamp = ts.index[2]
print(ts[stamp])
print(ts['1/10/2011'])
print(ts['20110110'], '\n')

longer_ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(longer_ts, '\n')
print(longer_ts['2001'], '\n')
print(longer_ts['2001-05'], '\n')

print(ts[datetime(2011, 1, 7):], '\n')
print(ts['1/6/2011':'1/11/2011'], '\n')
print(ts.truncate(after='1/9/2011'), '\n')

dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4), index=dates,
                       columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(long_df.loc['5-2001'])