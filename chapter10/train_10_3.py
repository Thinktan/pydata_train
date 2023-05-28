import pandas as pd
import numpy as np

tips = pd.read_csv('../examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']

def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]

print(top(tips, n=6), '\n')

smokerGroupBy = tips.groupby('smoker')

for k, g in smokerGroupBy:
    print(k)
    print(g, '\n')

print(smokerGroupBy.apply(top), '\n')
print(smokerGroupBy.count(), '\n')

print(tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill'), '\n')
print(tips.groupby(['smoker', 'day']).apply(top, n=2, column='total_bill'), '\n')

print('------smoker tip_pct describe-----')
result = tips.groupby('smoker')['tip_pct'].describe()
print(result, '\n-----------------------------\n')
print(result.unstack('smoker'), '\n')
print(type(result.unstack('smoker')))
