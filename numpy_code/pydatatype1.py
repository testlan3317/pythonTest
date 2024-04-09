"""
By default Python have these data types:
strings - used to represent text data.
integer - used to represent integer numbers. e.g. -1,-2,-3
float - used to represent numbers
boolean - used to represent True or False
complex - used to represent complex numbers. e.g. 1.0+2.0j, 1.5+2.5j

Numpy has some extra data types, and refer to data types with one character, like 
i - integer    u - unsigned integer
b - boolean    f - float  c - complex float  m - timedelta
M - datetime   O - object S - string  U - unicode string  V - fixed chunk of memory for other type

"""

import numpy as np

arr = np.array([1,2,3,4,5])

# dtype: returns the data type of the array
print(arr.dtype)

# dtype: allows us to define the expected data type of the array elements
arr1 = np.array([1,2,3,4], dtype='S')

print(arr1)
print(arr1.dtype)


arr2 = np.array([1.1,2,1,3.1])

# the best way to change the data type of an existing array, is to make a copy of the
# array with the astype() method.

newarr = arr2.astype('i') # or astype(int) works too, but returns int64
print(newarr)
print(newarr.dtype)   # return int32


