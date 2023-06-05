import pandas as pd
import numpy as np

# 从数组生成PeriodIndex

data = pd.read_csv('../examples/macrodata.csv')
print(data)
print(data.year)
print(data.quarter)

index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq='Q-DEC')
print(index)
data.index = index
print(data.infl)