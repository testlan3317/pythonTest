# remove(), pop() element
# Elements can be removed from the array by using built-in remove() function but an Error araises if element doesn't exist in the set.

# remove() only removes one element at a time, to remove range of elements, iterator is used. 

# pop() can also be sued to remove and return an element from the array, but by default it removes only the last element of the array. 

# to remove element from a specific position of the array, index of the element is passed as an argument to the pop() method.

# Note - Remove method in List will only remove the first occurrence  of the searched element.

import array

arr = array.array('i', [1, 2, 3, 1, 5])

# printing original array
print("The new created array is: ", end =" ")
for i in range(0, 5):
    print(arr[i], end=" ")
print("\r")

# using pop() to remove element at 2nd position
print("The poped element is: ", end="")
print(arr.pop(2))

# printing array after popping
print("The array after poping is: ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")
print("\r")

# using remove() to remove 1st occurence of 1
arr.remove(1)
# printing array after removing
print("The array after poping is: ", end="")
for i in range(0, 3):
    print(arr[i], end = " ")
print("\r")

