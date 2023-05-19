
import pandas as pd
import numpy as np

data = pd.Series(np.random.rand(9),
                 index = [['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                          [1, 2, 3, 1, 3, 1, 2, 2, 3]])

print(data, '\n')
print(data.index, '\n')
print(data['b'], '\n')
print(data['b':'c'], '\n')
print(data.loc[['b', 'c']], '\n')
print(data.loc[:, 2], '\n')

print(data.unstack(), '\n')
print(data.unstack().stack(), '\n')

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])

print(frame, '\n')

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)

print(frame['Ohio'], '\n')
