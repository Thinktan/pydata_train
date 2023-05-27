import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

tips = pd.read_csv('../examples/tips.csv')
tips['tip_pct'] = tips['tip'] / (tips['total_bill']-tips['tip'])

print(tips.columns, '\n')
print(tips['day'].value_counts(), '\n')
print(tips['time'].value_counts(), '\n')
print(tips['smoker'].value_counts(), '\n')

# sb.catplot(x='day', y='tip_pct', hue='time', col='smoker',
#               kind='bar', data=tips[tips.tip_pct < 1])
sb.catplot(x='day', y='tip_pct', row='time', col='smoker',
              kind='bar', data=tips[tips.tip_pct < 1])

plt.show()
