import pandas as pd
import numpy as np

tips = pd.read_csv('../examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']

print(tips.head(), '\n')

# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker'), '\n')
print(tips.pivot_table(values=['tip_pct', 'size'], index=['time', 'day'], columns='smoker').columns, '\n')
# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True), '\n')

print(tips.pivot_table(index=['time', 'smoker'], columns='day', values='tip_pct', aggfunc=len, margins=True), '\n')

