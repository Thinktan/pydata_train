import numpy as np
import pandas as pd

# 分类数据 背景与目标

values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
print(values, '\n')
print(pd.unique(values), '\n')
print(pd.value_counts(values), '\n')

# 重复值的标识方法，使用维度表，数据表的值是维度表的键
values = pd.Series([0, 1, 0, 0] * 2)
dim = pd.Series(['apple', 'orange'])
print(dim.take(values))