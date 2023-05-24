import matplotlib.pyplot as plt
import numpy as np

# 方法1:创建图片figure以及添加子图subplot
# fig = plt.figure()
#
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)

# 绘图1:plt.plot会最后一个图片和子图(如果需要就创建一个，比如没有add_subplot情况下)上进行绘制
# plt.plot(np.random.randn(50).cumsum(), 'k--')

# 绘图2: 直接使用Subplot对象进行绘制
# _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))

# 方法2:
fig, axes = plt.subplots(2, 3)

# 绘图1:plt.plot会最后一个图片和子图(如果需要就创建一个，比如没有add_subplot情况下)上进行绘制
plt.plot(np.random.randn(50).cumsum(), 'k--')

# 绘图2: 直接使用Subplot对象进行绘制
_ = axes[0][2].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
axes[0][0].scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))

plt.show()