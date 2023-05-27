import pandas as pd
import numpy as np

tips = pd.read_csv('../examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']
print(tips[:6], '\n')

grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
print(grouped_pct, '\n')

# for x, y in grouped_pct:
#     print(x)
#     print(y, '\n')

print(grouped_pct.agg('mean'), '\n')

print(grouped_pct.agg(['mean', 'std']), '\n')

print(grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]))


functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
# 产生的DataFrame拥有分层列，与分别聚合每一列，
# 再以列名作为keys参数使用concat将结果拼接在一起的结果相同
print(result, '\n')

print(grouped['tip_pct', 'total_bill'], '\n')
for (k1, k2), g in grouped['tip_pct', 'total_bill']:
    print(k1, k2)
    print(g.head(), '\n')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

for (k1, k2), g in grouped:
    print(k1, k2)
    print(g.head(), '\n')

# 对不同的列使用不同的方法
print(grouped.agg({'tip': np.max, 'size': 'sum'}), '\n')
print(grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'],
                   'size': 'sum'}), '\n')

print('===================================')
print(tips.groupby(['day', 'smoker'], as_index=False).mean(), '\n')
print(tips.groupby(['day', 'smoker']).mean(), '\n')