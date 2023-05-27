import numpy as np
import pandas as pd

# 根据索引层级分组

columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                     [1, 3, 5, 1, 3]],
                                    names=['cty', 'tenor'])

hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
print(hier_df, '\n')

for k, g in hier_df.groupby(level='cty', axis=1):
    print(k)
    print(g, '\n')

print(hier_df.groupby(level='cty', axis=1).mean())