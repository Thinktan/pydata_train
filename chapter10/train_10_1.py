
import pandas as pd
import numpy as np


df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'date2': np.random.randn(5)})

print(df, '\n')

grouped = df['data1'].groupby(df['key1'])
print(grouped, '\n')
print(grouped.mean())

means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(means, '\n')
print(means.unstack(), '\n')

print(df['data1'], '\n')

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])

print(df['data1'].groupby([states, years]).mean(), '\n')

print(df.groupby(['key1', 'key2']).size(), '\n')

