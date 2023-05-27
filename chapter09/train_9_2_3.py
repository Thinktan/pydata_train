
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# tips = pd.read_csv('../examples/tips.csv')
# tips['tip_pct'] = tips['tip'] / (tips['total_bill']-tips['tip'])
# tips['tip_pct'].plot.hist(bins=50)
# tips['tip_pct'].plot.density()
# plt.show()

comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)

values = pd.Series(np.concatenate([comp1, comp2]))
sb.distplot(values, bins=100, color='k')
plt.show()