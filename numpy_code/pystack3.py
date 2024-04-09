# Numpy provides a helper function: dstack() to stack along height, which is the same as depth
# which means, if the array len is 3, the depth would be 3. top-bottom

# by default, np.stack((a,b))  return 2-D array
# np.concatenate((a,b))  return 1-D array


import numpy as np

arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.dstack((arr1,arr2))

print(arr)
