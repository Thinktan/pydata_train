import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe(), '\n')

col = data[2]
print(col[np.abs(col)>3], '\n')

# 选出绝对值大于3的行
print(data[(np.abs(data)>3).any(1)])

print(data.shape, '\n-------\n')
print(np.sign(data).shape, '\n-------\n')
print((np.abs(data)>3).shape, '\n-------\n')
print(data[np.abs(data)>3].shape, '\n-------\n')

print(data.head, '\n-------\n')
print((np.sign(data)*3).head, '\n-------\n')
print((np.abs(data)>3).head, '\n-------\n')
#print((np.abs(data)>3).describe(), '\n-------\n')
print(data[np.abs(data)>3].head, '\n-------\n')

data[np.abs(data)>3] = np.sign(data) * 3
print(data.head)




