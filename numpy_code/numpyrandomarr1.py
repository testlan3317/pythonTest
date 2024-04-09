# choice() method allows you to generate a random value based on an array of values. 

from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)

# add a size parameter to specify the output shape.

x1 = random.choice([3,5,6,7], size=(3,5))

print(x1)
