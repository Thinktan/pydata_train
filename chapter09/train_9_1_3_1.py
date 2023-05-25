import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

seed_value = 42
np.random.seed(seed_value)
data = np.random.randn(1000).cumsum()
print(data)

ax.plot(data)

ticks = ax.set_xticks([0, 250, 500, 750, 1000])
# ticks = ax.set_xticks([250, 500, 750, 1000, 1250])
# 这个即使不在data索引范围内，也会展示全部data，这个只做为刻度使用
# labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
ax.set_title("My first matplotlib plot")
ax.set_xlabel('Stage')

plt.show()