
import pandas as pd
from numpy import nan as NA

# string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])

data = pd.DataFrame([[1., 6.5, 3.], [1, NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
print(data, '\n')

cleaned = data.dropna()
print(cleaned, '\n')

cleaned = data.dropna(how='all')
print(cleaned, '\n')