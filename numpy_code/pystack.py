# stacking is same as concatenation, the only difference is that stacking is done along a new axis.



import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr3 = np.stack((arr1,arr2), axis=1)

arr4 = np.stack((arr1,arr2))  # if axis is not explicitly passed it is taken as 0.

print(arr3)
print(arr4)
