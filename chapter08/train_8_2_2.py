
import pandas as pd
import numpy as np

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})

right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

print(left1, '\n')
print(right1, '\n')

print(pd.merge(left1, right1, left_on='key', right_index=True), '\n')
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'), '\n')

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})

righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])

print(lefth, '\n')
print(righth, '\n')

# left用列，right用index
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True), '\n')

# left和right都用index
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])

right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])

print(pd.merge(left2, right2, how='outer', left_index=True, right_index=True), '\n')

# 使用调用DataFrame的某一列连接传递的DataFrame的索引
print(left1.join(right1, on='key'), '\n')


another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York', 'Oregon'])

print(left2, '\n')
print(right2, '\n')
print(another, '\n')

print(left2.join([right2, another]), '\n')
print(left2.join([right2, another], how='outer'), '\n')
