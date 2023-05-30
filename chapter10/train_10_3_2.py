import pandas as pd
import numpy as np

frame = pd.DataFrame({'data1': np.random.randn(1000),
                      'data2': np.random.randn(1000)})

quartiles = pd.cut(frame.data1, 4)
print(quartiles[:5], '\n')

# print(frame.data1.head(), '\n')

def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}

group = frame.data1.groupby(quartiles)
# print(group, '\n')
# for k, v in group:
#     print(k)
#     print(v, '\n')

print(group.apply(get_stats).unstack(), '\n')

# grouping = pd.qcut(frame.data1, 10, labels=False)
# print(grouping, '\n')