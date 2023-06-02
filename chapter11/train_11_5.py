import pandas as pd

p = pd.Period(2007, freq='A-DEC')
print(p)
print(p+5)
print(p-2)
print(pd.Period(2014, freq='A-DEC')-p)

rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
print(rng)

values = ['2001Q3', '2002Q2', '2003Q1']
index = pd.PeriodIndex(values, freq='Q-DEC')
print(index)
