
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

data = pd.read_csv('../examples/spx.csv', index_col=0, parse_dates=True)
spx = data['SPX']
print(data.head(), '\n')
print(data['SPX'].head(), '\n')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# ax.plot(data, 'k-')
spx.plot(ax=ax, style='k-')

crisis_data = [
    (datetime(2007, 10, 11), 'Peak of bull market'),
    (datetime(2008, 3, 12), "Bear Stearns Fails"),
    (datetime(2008, 9, 15), "Lehman Bankruptcy")
]



# - `xy`: 这是注释的目标点的坐标（x, y）。它指定了注释文本箭头的起始位置。
# - `xytext`: 这是注释文本的坐标（x, y）。它指定了注释文本的位置，即文本的起始点。
# - `arrowprops`: 这是一个可选参数，用于设置注释箭头的样式和属性。你可以使用它来控制箭头的颜色、线宽、风格等。
# - `horizontalalignment`: 这是注释文本的水平对齐方式。可选值有'center'（居中对齐，默认值）、'left'（左对齐）和'right'（右对齐）。
# - `verticalalignment`: 这是注释文本的垂直对齐方式。可选值有'center'（居中对齐，默认值）、'top'（顶部对齐）和'bottom'（底部对齐）。


for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 75),
                xytext=(date, spx.asof(date) + 225),
                arrowprops=dict(facecolor='black',  headwidth=4, width=2, headlength=4),
                horizontalalignment='left', verticalalignment='top')

# 放大2007年～2010年
ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])
ax.set_title('Important dates in the 2008-2009 financial crisis')

plt.show()

# demo 2
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
plt.show()