import pandas as pd
import numpy as np

data = pd.DataFrame({'k1': ['one', 'two']*3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data, '\n')
print(data.duplicated(), '\n')
print(data.drop_duplicates(), '\n')
print(data, '\n')

data['v1'] = range(7)
print(data, '\n')
print(data.drop_duplicates(['k1']), '\n')

# keep = False，删除所有重复的项。
# 就是我拿到了一张考研录取名单df，和一个复试名单new_df，我先用df_process = new_df.append(df)，
# 再df_process.drop_duplicates(keep=False,inplace=True)。我就得到复试被刷的名单了。

