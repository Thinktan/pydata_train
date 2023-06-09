import pandas as pd
import numpy as np

# pandas与建模代码的结合

data = pd.DataFrame({
    'x0': [1, 2, 3, 4, 5],
    'x1': [0.01, -0.01, 0.25, -4.1, 0.],
    'y': [-1.5, 0., 3.6, 1.3, -2.]})

print(data, '\n')
print(data.columns, '\n')
print(data.index, '\n')
print(data.values, '\n')
