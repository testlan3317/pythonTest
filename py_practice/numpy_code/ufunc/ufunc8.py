# what is a set
# a set in mathematics is a collection of unique elements
# for operations involving frequent intersection, union and difference operations.

import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)

# find intersection
# intersect1d()
newarr1 = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr1)

# assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.

# find difference
# setdiff1d()
newarr2 = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr2)

# Finding Symmetric Difference
# setxor1d()
newarr3 = np.setxor1d(arr1, arr2, assume_unique=True)
print(newarr3)

