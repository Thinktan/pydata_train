import pandas as pd
import numpy as np

# 使用区间进行重新采样
frame = pd.DataFrame(np.random.randn(24, 4),
                     index=pd.period_range('1-2000', '12-2001', freq='M'),
                     columns=['Colorado', 'Texas', 'New York', "Ohio"])

print(frame, '\n')

# 向下采样 月 -> 年
annual_frame = frame.resample('A-DEC').mean()
print(annual_frame, '\n')

# 向上采样 年 -> 季度
# convention参数，只有在对时间区间索引进行向上重采样时，才有用。
# 例如，把原频率是年的索引，向上采样为季度，
# convention默认为start，意味着当年的数据，放在当年的第一个季度。
# 如果为end则放在当年的最后一个季度。
print(annual_frame.resample('Q-DEC').ffill(), '\n')
print(annual_frame.resample('Q-DEC', convention='end').ffill(), '\n')











