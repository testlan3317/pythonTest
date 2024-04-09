# LCM: Lowest Common Multiple (zui xiao gong bei shu)
# GCD: Greatest Common Denominator (zui da gong yue shu)

import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print(x)

# Finding LCM in Arrays
# To find the Lowest Common Multiple of all values in an array, you can use the "reduce()" mothod
arr = np.array([3, 6, 9])
x1 = np.lcm.reduce(arr)
print(x1)

# arange(1, 11) : find all values of an array where the array contains all integers from 1 to 10
arr1 = np.arange(1,11)
x2 = np.lcm.reduce(arr)
print(x2)

print("========Great Common Denomiator========")

num3 = 6
num4 = 9
x3 = np.gcd(num3, num4)
print(x3)

# Finding GCD in Arrays
arr2 = np.array([20, 8, 32,36, 16])
x4 = np.gcd.reduce(arr2)
print(x4)
