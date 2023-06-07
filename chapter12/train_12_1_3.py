import pandas as pd
import numpy as np

# 使用 Categorical 对象进行计算

np.random.seed(12345)
draws = np.random.randn(1000)

# bins = pd.qcut(draws, 4)
bins = pd.qcut(draws, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print(bins, '\n')
print(bins.value_counts())
print(type(bins), '\n')

bins = pd.Series(bins, name='quartile')
result = pd.Series(draws).groupby(bins).agg(['count', 'min', 'max'])

print(result)


















