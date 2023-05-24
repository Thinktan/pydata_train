from numpy.random import randn
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# data = np.random.randn(5)
# print(data, '\n')
# print(data.cumsum(), '\n')

# ax.plot(randn(1000).cumsum(), 'k')
# ax.plot(randn(1000).cumsum(), 'k', label='_nolegend_')
ax.plot(randn(1000).cumsum(), 'k', label='one')
ax.plot(randn(1000).cumsum(), 'k--', label='two')
ax.plot(randn(1000).cumsum(), 'k.', label='three')

ax.legend(loc='best')

plt.show()













