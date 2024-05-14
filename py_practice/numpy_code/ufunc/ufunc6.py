# Differences
# A discrete difference means substracting two successive elements
# e.g. [1,2,3,4], the discrete difference would be [2-1, 3-2, 4-3] = [1,1,1]
# To find the discrete difference, use the diff() function

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)

# compute discrete differenct twice
newarr1 = np.diff(arr, n = 2)

print(newarr1)
# returns [5 -30] because: 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30
