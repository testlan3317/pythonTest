# Binomial Distribution is a Discrete Distribution.
# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails. 
# It has 3 parameters:
# n - number of trails
# p - probability of occurence of each trail (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.

# Discrete Distribution: The distribution is defined at separate set of events. e.g. a coin toss's result is discrete as it can
# be only head or tails whereas height of people is continuous as it can be 170, 170.1, 170.11 and so on.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# kde: is a way to estimate the probability density function of a continuous random variable.
# if set kde = False, the curve will disappear, only left the histogram.

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

#sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=True)
plt.show()
