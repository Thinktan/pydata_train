
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

macro = pd.read_csv('../examples/macrodata.csv')
print(macro.head(), '\n')
print(macro.columns, '\n')

data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
print(trans_data.head())
# sb.regplot(x=trans_data['m1'], y=trans_data['unemp'])
# plt.title('Changes in log %s versus log %s' % ('m1', 'unemp'))

sb.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})

plt.show()