import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 二元移动窗口函数

close_px_all = pd.read_csv('../examples/stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]

spx_rets = close_px_all['SPX']
returns = close_px.pct_change()
print(spx_rets.shape)
print(returns.shape)
print(returns.AAPL.rolling(125, min_periods=100))


# corr = returns.AAPL.rolling(125, min_periods=100).corr(spx_rets)
# corr.plot()
# plt.show()
# print(returns.rolling(125, min_periods=100))


# corr = returns.rolling(125, min_periods=100).corr(spx_rets)
# corr.plot()
# plt.show()


