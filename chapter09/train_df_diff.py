import pandas as pd

df = pd.DataFrame({'A': [1, 2, 5, 8, 15],
                   'B': [5, 15, 23, 21, 54]})

print(df.diff().dropna())