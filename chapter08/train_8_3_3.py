
import numpy as np
import pandas as pd

df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

print(df, '\n')

melted = pd.melt(df, ['key'])
print(melted, '\n')

reshaped = melted.pivot('key', 'variable', 'value')
print(reshaped, '\n')

print(reshaped.reset_index(), '\n')

print(df, '\n')

print(pd.melt(df, id_vars=['key'], value_vars=['A', 'B']), '\n')

print(pd.melt(df, value_vars=['A', 'B', 'C']), '\n')

print(pd.melt(df, value_vars=['key', 'A', 'B']), '\n')














