import pandas as pd
import numpy as np

# 向上采样与插值

frame = pd.DataFrame(np.random.randn(2, 4),
                    index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
                    columns=['Colorado', 'Texas', 'New York', 'Ohio'])

print(frame, '\n')

# asfreq 方法可以理解成“生成数据”这个动作，resample 类比于定义了一个类，
# asfreq 类比于使用 new 关键字创建一个对象。

# 填充
print(frame.resample('D').asfreq(), '\n')
print(frame.resample('D').ffill(), '\n')
print(frame.resample('D').ffill(limit=2), '\n')
print(frame.resample('W-THU').asfreq(), '\n')
print(frame.resample('W-THU').ffill(), '\n')