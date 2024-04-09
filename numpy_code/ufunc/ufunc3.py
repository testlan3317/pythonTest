# Arithmetic

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])

arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)

# returned [30 32 34 36 38 40] which is the sums of 10+20, 11+21, 12+22 etc

newarr1 = np.subtract(arr2, arr1)

print(newarr1)

newarr2 = np.multiply(arr1, arr2)

print(newarr2)

newarr3 = np.divide(arr1, arr2)
print(newarr3)


