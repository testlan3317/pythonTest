# Find the indexes where the values 2,4 and 6 should be inserted

import numpy as np

arr = np.array([1,3,5,7])

x = np.searchsorted(arr, [2,4,6])

print(x)

# The return value is an array: [1 2 3] containing the three indexes where 2,4,6 would be inserted in the original array to maintain the order.
