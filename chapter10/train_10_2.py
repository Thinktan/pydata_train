import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})

print(df, '\n')

grouped = df.groupby('key1')

print(grouped['data1'].quantile(0.9), '\n')
print(grouped[['data1']].quantile(0.9), '\n')
print(grouped[['data1', 'data2']].quantile(0.9), '\n')

def peak_to_peak(arr):
    return arr.max() - arr.min()

print('----------------')

print(grouped.agg(peak_to_peak), '\n')

print('----------------')

print(grouped.describe(), '\n')

for x, y in grouped.describe():
    print(x)
    print(y, '\n')

