import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 自定义移动窗口函数

close_px_all = pd.read_csv('../examples/stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]

spx_rets = close_px_all['SPX']
returns = close_px.pct_change()


from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
result.plot()
plt.show()
