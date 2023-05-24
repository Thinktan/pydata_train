from numpy.random import randn
import matplotlib.pyplot as plt

# plt.plot(randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
# plt.show()

data = randn(30).cumsum()
print(data)
plt.plot(data, 'k--', label='Default')

plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')

plt.legend(loc='best')

plt.show()
