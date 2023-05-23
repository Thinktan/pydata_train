import matplotlib.pyplot as plt
import numpy as np

# 创建图片figure
fig = plt.figure()

# 创建子图subplot
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)

# 绘图1:plt.plot会最后一个图片和子图(如果需要就创建一个，比如没有add_subplot情况下)上进行绘制
plt.plot(np.random.randn(50).cumsum(), 'k--')

# 绘图2: 直接使用Subplot对象进行绘制


plt.show()