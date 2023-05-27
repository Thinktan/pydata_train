import numpy as np
import pandas as pd

people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

people.iloc[2:3, [1, 2]] = np.nan
print(people, '\n')

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'}

by_column = people.groupby(mapping, axis=1)

for k, v in by_column:
    print(k)
    print(v, '\n')

print(by_column.sum(), '\n')

map_series = pd.Series(mapping)
print(map_series, '\n')
print(people.groupby(map_series, axis=1).count(), '\n')
