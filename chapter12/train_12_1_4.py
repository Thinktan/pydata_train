import numpy as np
import pandas as pd

# 分类方法
s = pd.Series(['a', 'b', 'c', 'd']*2)
cat_s = s.astype('category')
print(cat_s, '\n')

# 特殊属性cat提供了对分类方法的访问
# 方便将分类数据转换为数值型数据，方便后续急需处理 s
print(cat_s.cat.codes, '\n')
print(cat_s.cat.categories, '\n----')

# 使用 set_categories 方法改变类别
actual_categories = ['a', 'b', 'c', 'd', 'e']
cat_s2 = cat_s.cat.set_categories(actual_categories)
print(cat_s2, '\n')
print(cat_s.value_counts(), '\n')
print(cat_s2.value_counts(), '\n')

# 使用remove_unused_categories方法移除未用到的类别
cat_s3 = cat_s[cat_s.isin(['a', 'b'])]
print(cat_s3, '\n')
print(cat_s3.cat.remove_unused_categories())

