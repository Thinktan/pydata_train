
import pandas as pd
from numpy import nan as NA

# string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])

data = pd.DataFrame([[1., 6.5, 3.], [1, NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
print(data, '\n')

cleaned = data.dropna()
print(cleaned, '\n')

cleaned = data.dropna(how='all')
print(cleaned, '\n')

print(data, '\n')

data[4] = NA
cleaned = data.dropna(axis=1, how='all')
print(cleaned, '\n')

import numpy as np
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df, '\n')
print(df.dropna(), '\n')
print(df.dropna(thresh=2), '\n')

print(df.fillna(0), '\n')

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[1:3, 1] = NA
df.iloc[4:6, 1] = NA
print(df, '\n')
print(df.fillna(method='ffill', limit=1))

