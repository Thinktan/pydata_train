import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, sharex=False, sharey=True)

for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.rand(500), bins=50, color='k', alpha=0.5)

plt.subplots_adjust(wspace=0.1, hspace=0.1)

plt.show()