import pandas as pd

tips = pd.read_csv('../examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']

print(pd.crosstab([tips.time, tips.day], tips.smoker, margins=True), '\n')
print(pd.crosstab(tips.time, tips.smoker, margins=True), '\n')
print(pd.crosstab(tips.day, tips.smoker, margins=True), '\n')
