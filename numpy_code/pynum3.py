import numpy as np

arr = np.array([ [[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]] ])

print (arr)

#ndim: this attribute tells us how many dimensions the array have.
print(arr.ndim)

# create 5 dimensions array
# np.array([1,2,3,4,5], ndmin=5)

print(arr[1])
print(arr[1][1])
print(arr[1][1][1])
