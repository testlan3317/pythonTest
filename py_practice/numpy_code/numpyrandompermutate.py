#Random Permutations of Elements
# a permutation refers to an arrangement of elements. e.g. [3,2,1] is a permutation of [1,2,3] and vice-versa

# The NumPy Random module provides two methods for this: shuffle() and permutation()

from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])

random.shuffle(arr)

print(arr)

# note: shuffle() methods makes changes to the original array

arr1 = np.array([1,2,3,4,5])

print(random.permutation(arr1))

# note: permutation() method returns a re-arrange array ( the original array un-changed)


