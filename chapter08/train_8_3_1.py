
import pandas as pd
import numpy as np


# stack unstack
data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index = pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns = pd.Index(['one', 'two', 'three'], name = 'number'))

print(data, '\n')

result = data.stack()
print(result, '\n')
print(result.unstack(), '\n') # 默认最内层

# 传入层级序号或名称
print(result.unstack(0), '\n')
print(result.unstack('state'), '\n')

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])

print(data2, '\n')
print(data2.unstack(), '\n')
print(data2.unstack().stack(), '\n')

# 在DataFrame中拆堆时，被拆堆的层级会变为结果中最低的层级
df = pd.DataFrame({'left': result, 'right': result+5},
                  columns=pd.Index(['left', 'right'], name='side'))

print(df, '\n')
print(df.unstack('state'), '\n')
print(df.unstack('state').stack('side'), '\n')