# shape: this attribute returns a tuple with a number in each dimension

import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])

print(arr.shape)


# reshape: means chaing the shape of an array

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr1.reshape(4,3) # 4 - row 3-column

print(newarr)

# reshape 3d

arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr1 = arr2.reshape(2,3,2)  # 2-3D, 3-2D, 2-1D

print(newarr1)

# reshape has the base, reshape allow "unknown" dimension e.g. arr.reshape(2,2,-1)
# flatten: means convert multi-dimension array into 1D array
# use reshape(-1) to do this

arr3 = np.array([[1,2,3],[4,5,6]])

newarr2 = arr3.reshape(-1)
print(newarr2)
