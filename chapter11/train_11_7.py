import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 移动窗口函数
close_px_all = pd.read_csv('../examples/stock_px.csv', parse_dates=True, index_col=0)
print(close_px_all.columns)
print(len(close_px_all))

close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
print(close_px[0:10])
print('------------')
close_px = close_px.resample('B').ffill()
print(close_px[0:20])
print('------------')

# close_px.AAPL.plot()
# close_px.AAPL.rolling(250).mean().plot()
# plt.show()

# appl_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
appl_std250 = close_px.AAPL.rolling(250).std()
print(appl_std250[0:20], '\n')
# appl_std250.plot()
# plt.show()

# expanding_appl_std250 = appl_std250.expanding()
# print(expanding_appl_std250, '\n')
# appl_std250.rolling(60).mean().plot(logy=True)
# plt.show()


print(close_px.rolling('20D').mean(), '\n')




