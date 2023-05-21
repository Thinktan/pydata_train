
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])

print(frame, '\n')

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame, '\n')
print(frame.sort_index(level=1), '\n============\n')

# 在pandas的DataFrame中，`sort_index`方法是用来根据索引对数据进行排序的。这个方法中的`level`参数是用来指定多级索引中哪一级的索引用来进行排序的。
#
# 例如，如果你有一个双级（两层）索引的DataFrame，你可以通过设置`level=0`或者`level=1`来选择根据哪一级的索引进行排序。`level=0`将根据第一级的索引排序，而`level=1`将根据第二级的索引进行排序。
#
# 如果你想根据多个层级进行排序，你可以传入一个层级列表，如`level=[0, 1]`。这将首先根据第一级索引排序，然后在第一级索引相同的情况下，根据第二级索引进行排序。
#
# 总的来说，`level`参数就是用来指定你想根据哪些层级的索引进行排序的。
print(frame.swaplevel('key1', 'key2'), '\n')
print(frame.swaplevel(0, 1).sort_index(level=0), '\n')

