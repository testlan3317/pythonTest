#Filtering Arrays:
# Getting some elements out of an existing array and creating a new array out of them.

# you can filter the elements with a list of boolean value. if the value of the relative item is True, the element will be picked
# if False, then not pick it. 

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
