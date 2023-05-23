
import pandas as pd

df = pd.DataFrame({"A": [1 ,2, 3], "B": [7, 8, 9]},
                  index=['a', 'b', 'c'])
print(df, '\n')

columns = pd.Index(['A', 'D'], name='item')
print(df.reindex(columns=columns), '\n')