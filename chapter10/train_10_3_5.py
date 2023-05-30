
import numpy as np
import pandas as pd

# 分组加权平均和相关性

df = pd.DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                   'data': np.random.randn(8),
                   'weights': np.random.rand(8)})

# print(df, '\n')
# grouped = df.groupby('category')
# get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
# print(grouped.apply(get_wavg), '\n')

close_px = pd.read_csv('../examples/stock_px.csv', parse_dates=True, index_col=0)
# print(close_px.info(), '\n')

spx_corr = lambda x: x.corrwith(x['SPX'])
rets = close_px.pct_change().dropna()

get_year = lambda x: x.year
by_year = rets.groupby(get_year)
print(by_year, '\n')

# for k, g in by_year:
#     print(k)
#     print(g, '\n')

print(by_year.apply(spx_corr), '\n')

print(by_year.apply(lambda g: g['AAPL'].corr(g['MSFT'])), '\n')

