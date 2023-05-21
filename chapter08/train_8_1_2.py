
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame, '\n')

# 按层级进行汇总索引
print(frame.sum(level='key2'), '\n')

print(frame.sum(level='color', axis=1), '\n')