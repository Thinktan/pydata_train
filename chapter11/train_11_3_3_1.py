from datetime import datetime

import pandas as pd
from pandas.tseries.offsets import Day, MonthEnd
import numpy as np

now = datetime(2011, 11, 17)
print(now)
print(now + MonthEnd())
print(now + MonthEnd(2), '\n')

# 锚定偏置可以使用rollforward和rollback分别显式地将日期向前或向后"滚动"
offset = MonthEnd()
print(offset.rollforward(now))
print(offset.rollback(now), '\n')

# 对每个时间调用了MonthEnd进行偏移，使每个日期平移到了月末的那一天。
# 之后调用 groupby 时，就达到了按月分组的目的。
ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000', periods=20, freq='4d'))

print(ts.groupby(offset.rollforward).mean(), '\n')
print(ts.resample('M').mean(), '\n')