# Numpy work with arrays
# randint() takes a size parameter where you can specify the shape of an array

# randint(100, size=(5))   # 1-D 

from numpy import random

x = random.randint(100, size=(5))

print(x)

# randint(100, size=(3,5))  # 3 rows, 5 cols
# rand(size(3,5))

x1 = random.randint(100, size=(3,5))

print(x1)
