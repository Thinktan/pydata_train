
import numpy as np
import pandas as pd

# 显示设置
pd.options.display.max_rows = 4

result = pd.read_csv('../examples/ex6.csv')
print(result)

chunker = pd.read_csv('../examples/ex6.csv', chunksize=1000)
tot = pd.Series([])
for piece in chunker:
    # add函数将series或者dataframe中相交非空的部份求和
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)
print(tot)
