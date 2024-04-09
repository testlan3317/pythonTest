# you can search an array for a certain value, and return the indexes that get a match

# use where() method

import numpy as np

arr = np.array([1,2,3,4,5,4,4])

x = np.where(arr==4)

print(x)

# the example return a tuple: (array([3,5,6],))
# which means that the value 4 is present at index 3, 5, and 6.
