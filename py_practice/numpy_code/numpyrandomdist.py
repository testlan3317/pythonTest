# Random Distribution
# A random distribution is a set of random numbers that follow a certain probability density function.

# Probability Density Function: A function that describes a continuous probability.

# choice() method allows us to specify the probability for each value
# probability ise set by a number between 0 and 1. 0 means value never occur, 1 means the value will always occur

from numpy import random

# generate 1-d contains 100 values
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

# note: the sum of all probability numbers should be 1.

# add size to get output shape

x1 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x1)
