#Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

# Distplot: stands for distribution plot, it takes as input an array, and plot a curve corresponding to the distribution of pointsin the array

# distplot()

import matplotlib.pyplot as plt

import seaborn as sns

#sns.distplot([0,1,2,3,4,5])

#plt.show()

# Plotting a Distplot without the Histogram (Histogram: zhiFang Tu)

sns.distplot([0, 1,2,3,4,5], hist=False)

plt.show()
