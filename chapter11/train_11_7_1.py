
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 指数加权函数

close_px_all = pd.read_csv('../examples/stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
print(close_px, '\n')
aapl_px = close_px.AAPL['2006':'2007']

# 股票价格 60 日均线
ma60 = aapl_px.rolling(30, min_periods=20).mean()

# span=30 的EW 移动平均线
ewma60 = aapl_px.ewm(span=30).mean()

ma60.plot(style='k--', label='Simple MA')
ewma60.plot(style='k-', label='EW MA')
plt.legend()
plt.show()