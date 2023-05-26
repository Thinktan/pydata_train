
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# case1
# fig, axes = plt.subplots(2, 1)
# data = pd.Series(np.random.randn(16), index=list('abcdefghijklmnop'))
# data.plot.bar(ax=axes[0], color='k', alpha=0.7)
# data.plot.barh(ax=axes[1], color='k', alpha=0.7)
# plt.show()

# case2
df = pd.DataFrame(np.random.rand(6, 4),
                  index = ['one', 'two', 'three', 'four', 'five', 'six'],
                  columns = pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
# print(df, '\n')
# df.plot.bar()
# plt.show()

# df.plot.barh(stacked=True, alpha =0.5)
# plt.show()

# case3
tips = pd.read_csv('../examples/tips.csv')
# print(tips['size'].value_counts().sort_index(), '\n')
# print(tips['day'].value_counts().sort_index(), '\n')
# party_counts = pd.crosstab(tips['day'], tips['size'])
# print(party_counts, '\n')
# party_counts = party_counts.loc[:, 2:5]
# print(party_counts, '\n')
# print(party_counts.sum(1), '\n')
# party_pcts = party_counts.div(party_counts.sum(1), axis=0)
# print(party_pcts, '\n')
# party_pcts.plot.bar()
# plt.show()

# case4 use seaborn
tips['tip_pct'] = tips['tip'] / (tips['total_bill']-tips['tip'])
print(tips.head(), '\n')
print(tips[tips['day'] == 'Sun']['tip_pct'].mean(), '\n')

sb.barplot(x='tip_pct', y='day', data=tips, orient='h')
sb.set(style='whitegrid')
plt.show()





