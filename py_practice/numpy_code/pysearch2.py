# The Numpy searchsorted() function accepts four parameters(array, values, side,sorter) and first two are mandatory.

# searchsorted() function return the inserting index 2 for value 30, because 30 will be insert after 22 to maintain the sorted order of the array

import numpy as np

arr = np.array([6,7,8,9])

x = np.searchsorted(arr, 7)

print(x)

arr1 = np.array([11,22,33,44])

x1 = np.searchsorted(arr1,30)

print(x1)
