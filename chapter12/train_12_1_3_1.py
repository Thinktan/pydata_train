import pandas as pd
import numpy as np

# 使用分类数据提高性能

N = 10000000

draws = pd.Series(np.random.randn(N))
labels = pd.Series(['foo', 'bar', 'baz', 'qux'] * (N//4))
# print(labels, '\n')
categories = labels.astype('category')

print(labels.memory_usage(), '\n')
print(categories.memory_usage(), '\n')

