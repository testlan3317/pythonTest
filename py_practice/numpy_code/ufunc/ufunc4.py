# power() rises the values from the first array to the power of the values of the second array
# and return in a new array

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])

arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)

#return 10*10*10 etc

# Both mod() and remainder() functions return the remainder of the values in the first array corresponding the values
# in the second array, and return the results in a new array

newarr1 = np.mod(arr1, arr2)
print(newarr1)


# Quotient and Mod
# divmod() function return both the quotient and the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod

newarr2 = np.divmod(arr1, arr2)

print(newarr2)


# both absolute() and abs() do the same absolute operation element-wise, but we should use absolute() to avoid confusion with python's build-in math.abs()

arr3 = np.array([-1, -2, 1, 3, -4])
newarr3 = np.absolute(arr3)

print(newarr3)

## Rounding Decimals
# - truncation
# - fix
# - rounding
# - floor
# - ceil

#remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
arr4 = np.trunc([-3.1666, 3.667])

print(arr4)

# Rounding
# around()

arr4 = np.around(3.1666, 2)
print(arr4)
