
import pandas as pd
import numpy as np

data = pd.read_csv('../examples/macrodata.csv')

print(data, '\n')

periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
print(periods, '\n')
print(periods.to_timestamp('D', 'end'), '\n')

columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
print(columns, '\n')

data = data.reindex(columns=columns)
print(data, '\n')

data.index = periods.to_timestamp('D', 'end')
print(data, '\n')

# print(data.stack(), '\n')
# print(data.stack().reset_index(), '\n')

# reset_index 原有索引变成一列，新增数字索引
ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata, '\n')

# 如果不指定value，则column是一个MultiIndex
pivoted = ldata.pivot('date', 'item', 'value')
print(pivoted, '\n')

ldata['value2'] = np.random.randn(len(ldata))
print(ldata[:5], '\n')

pivoted = ldata.pivot('date', 'item')
print(pivoted[:5], '\n')

# pivot方法等价于使用set_index创建分层索引，然后调用unstack
print(ldata.set_index(['date', 'item']), '\n')
print(ldata.set_index(['date', 'item']).unstack('item'), '\n')












