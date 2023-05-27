import numpy as np
import pandas as pd

people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

print(people.groupby(len).sum(), '\n')

key_list = ['one', 'one', 'one', 'two', 'two']
print(people.groupby([len, key_list]).min(), '\n')
# 0Joe/2Wes/3im已经分到了一组, 1Steve一组, 4Travis一组
# 0 -> one, 2 -> one, 3 -> two
# 1 -> one
# 4 -> two

# 3 one
# 5 one
# 3 one
# 3 two
# 6 two