import pandas as pd
import numpy as np

# pandas中的Categorical类型

fruits = ['apple', 'orange', 'apple', 'apple'] * 2
N = len(fruits)

df = pd.DataFrame({'fruit': fruits,
                   'basket_id': np.arange(N),
                   'count': np.random.randint(3, 15, size=N),
                   'weight': np.random.uniform(0, 4, size=N)},
                   columns = ['basket_id', 'fruit', 'count', 'weight'])
print(df, '\n')

fruit_cat = df['fruit'].astype('category')
print(fruit_cat, '\n')

print(type(fruit_cat), '\n')
print(type(fruit_cat.values), '\n')

c = fruit_cat.values
print(c.categories)
print(c.codes, '\n')

df['fruit'] = df['fruit'].astype('category')
print(df.fruit, '\n')

# 从其他 Python 序列类型直接生成 pandas.Categorical
my_categories = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])
print(my_categories, '\n')

# 使用 from_codes构造函数
categories = ['foo', 'bar', 'baz']
codes = [0, 1, 2, 0, 0, 1]
my_cat_2 = pd.Categorical.from_codes(codes, categories)
print(my_cat_2, '\n')

# 给类别进行排序
ordered_cat = pd.Categorical.from_codes(codes, categories, ordered=True)
print(ordered_cat, '\n')

# 将一个未排序的分类实例使用 as_ordered 进行排序 s
print(my_cat_2.as_ordered())













