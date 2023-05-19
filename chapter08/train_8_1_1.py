
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])

print(frame, '\n')

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)