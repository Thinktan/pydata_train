from datetime import datetime

# 字符串和datetime互相转换

stamp = datetime(2011, 1, 3)
print(str(stamp))
print(stamp.strftime('%Y-%m-%d'))

print('---------------------')

value = '2011-01-03'
print(datetime.strptime(value, '%Y-%m-%d'))

datestrs = ['7/6/2011', '8/6/2011']
print([datetime.strptime(x, '%m/%d/%Y') for x in datestrs])

print('---------------------')

import pandas as pd
datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
print(pd.to_datetime(datestrs))

idx = pd.to_datetime(datestrs + [None])
print(idx)
print(idx[2])
print(pd.isnull(idx))