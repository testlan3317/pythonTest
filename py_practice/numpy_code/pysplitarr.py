# splitting is reverse operation of Joining
# array_split() for splitting arrays, we pass the arr and the numbers we wants to split

# if the array has less elements than the number required, it will adjust from the end accordingly.

import numpy as np

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,3 )

print(newarr)

print("type of newarr: " + str(type(newarr)))
print(newarr[0])

print("type of newarr[0]: " + str(type(newarr[0])))
