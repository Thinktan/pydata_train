
import pandas as pd
import numpy as np

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)
print(cats.dtype, '\n')
print(cats, '\n')
print(pd.value_counts(cats.codes), '\n')

# right 开闭区间设置
ages2 = pd.cut(ages, [18, 26, 36, 61, 100], right=False)
print(ages2, '\n')

# labels: 自定义箱名
group_names = ['Youth', 'youngAdult', 'MiddleAged', 'Senior']
ages3 = pd.cut(ages, bins, labels=group_names)
print(ages3, '\n')

# 自定义箱数：根据最大最小值等分
data = np.random.rand(20)
print( pd.cut(data, 4, precision=2), '\n' )

# 根据样本分位数分箱
data = np.random.randn(1000)
cats = pd.qcut(data, 4) # 切成4分，25% 50% 75% 100%
print(cats, '\n')
print(pd.value_counts(cats).sort_index(), '\n')

# 自定义分位数
cats = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
print(cats, '\n')
print(pd.value_counts(cats).sort_index(), '\n')
