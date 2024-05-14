# The normal distribution is also called Gaussian Distribution.
# random.normal()
# random.normal(loc, scale, size)
# loc - (Mean) where the peak of the bell exists
# scale - (standard deviation) how falt the graph distribution should be
# size - the shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a random normal distribution of size 2*3
x = random.normal(size=(2, 3))

print(x)

# Generate a random normal distribution of size 2*3 with mean at 1 and standard devication of 2 (deviation: wu cha zhi)
x1 = random.normal(loc=1, scale=2, size=(2,3))

print(x1)

sns.distplot(x1, hist=False)
plt.show()

