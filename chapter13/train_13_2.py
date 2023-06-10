
import pandas as pd
import numpy as np
import patsy

# 13.2 使用Patsy创建模型描述

data = pd.DataFrame({
        'x0': [1, 2, 3, 4, 5],
        'x1': [0.01, -0.01, 0.25, -4.1, 0.],
        'y': [-1.5, 0., 3.6, 1.3, -2.]})
print(data, '\n')




y, X = patsy.dmatrices('y~x0 + x1', data)
print('X:')
print(X, '\n')
print('y:')
print(y, '\n')

coef, resid, _, _ = np.linalg.lstsq(X, y)
print('coef:\n', coef, '\n')

coef = pd.Series(coef.squeeze(), index=X.design_info.column_names)
print('coef:\n', coef, '\n')

# 13.2.1 Patsy公式中的数据转换
print('-------------13.2.1-------------')
y, X = patsy.dmatrices('y~x0 + np.log(np.abs(x1)+1)', data)
print('X:')
print(X, '\n')

y, X = patsy.dmatrices('y~standardize(x0) + center(x1)', data)
print('X:')
print(X, '\n')

print(X.design_info, '\n')

# patsy.build_design_matrices函数可以使用原始样本内数据集中保存的信息将变换应用于新的样本外数据上
new_data = pd.DataFrame({
        'x0': [6, 7, 8, 9],
        'x1': [3.1, -0.5, 0, 2.3],
        'y': [1, 2, 3, 4]})

new_X = patsy.build_design_matrices([X.design_info], new_data)
print('new_X:\n', new_X, '\n')

# I函数封装加法
y, X = patsy.dmatrices('y~I(x0+x1)', data)
print(X, '\n')

# 13.2.2 分类数据与Patsy
print('-------------13.2.2-------------')

data = pd.DataFrame({
        'key1': ['a', 'a', 'b', 'b', 'a', 'b', 'a', 'b'],
        'key2': [0, 1, 0, 1, 0, 1, 0, 0],
        'v1': [1, 2, 3, 4, 5, 6, 7, 8],
        'v2': [-1, 0, 2.5, -0.5, 4.0, -1.2, 0.2, -1.7]
})

y, X = patsy.dmatrices('v2~key1', data)
print('X:\n', X, '\n')

# 忽略截距
y, X = patsy.dmatrices('v2~key1+0', data)
print('X:\n', X, '\n')

# 使用C函数将数字列转成分类类型
y, X = patsy.dmatrices('v2~C(key2)', data)
print('X:\n', X, '\n')



# ANOVA方差模型
data['key2'] = data['key2'].map({0: 'zero', 1: 'one'})
print('data:\n', data, '\n')

y, X = patsy.dmatrices('v2~key1+key2', data)
print("X:\n", X, '\n')













