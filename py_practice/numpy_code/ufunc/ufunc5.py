# Summations:
# Addition is done between two arguments whereas summation happens over n elements.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)
# return [2 4 6]

newarr1 = np.sum([arr1, arr2])
print(newarr1)   # return 12

# Summation Over an Axis
# If you specify axis=1, NumPy will sum the numbers in each array.

newarr2 = np.sum([arr1, arr2], axis=1)

print(newarr2)  # return [6 6]

# Cummulative Sum
# e.g. The partial sum of [1,2,3,4] would be [1, 1+2, 1+2+3, 1+2+3+4]
# cumsum()

arr3 = np.array([1,2,3])
newarr3 = np.cumsum(arr3)

print(newarr3)

# Products:
# To find the product of the elements in an array, use the prod() function

arr4 = np.array([1,2,3,4])
x = np.prod(arr4)
print(x)

#return: 24 because 1*2*3*4

# on two arrays
x1 = np.prod([arr1, arr2])

print(x1)

# Product over an Axis
newarr4 = np.prod([arr1, arr2], axis=1)

print(newarr4)


#Cummulative Product
# Cummulative product means taking the product partially. 
# e.g. The partial product of [1,2,3,4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1,2,6,24]

newarr5 = np.cumprod(arr4)

print(newarr5)
