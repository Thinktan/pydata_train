import pandas as pd
import numpy as np

# 创建一个日期范围
rng = pd.date_range('1/1/2000', periods=9, freq='T')

# 创建一个简单的数据框
df = pd.DataFrame(np.random.randn(9, 3), index=rng, columns=['A', 'B', 'C'])
print(df, '\n')

# 对数据进行重采样，返回 period-based 的索引
resampled = df.resample('3T', kind='period')
print(resampled.sum())