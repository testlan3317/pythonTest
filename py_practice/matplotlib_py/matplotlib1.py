# subplot(nrows, ncols, index, **kwargs)
# it describes the display Grid. (nrows- row, ncols-col, index- which one)

# Matplotlib Subplot

import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,1,1)
plt.plot(x,y)

# plot2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x, y)

plt.show()
