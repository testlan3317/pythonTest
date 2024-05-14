# Array
# An array is a collection of items stored at contiguous memory locations.
# The idea is to store multiple items of the same type together. 
# This makes it easier to calculate the position of each element by simply adding an offset to a base value, 
# i.e, the memory location of the first element of the array

# Array can be handled in Python by a module named "array", they can be useful when we have to manipulate only a specific data type values.

# syntax: array(data_type, value_list)

import array as arr

# creating an array with integer type
a = arr.array('i', [1,2,3])

print("The new created array is: ", end=" ")
for i in range(0,3):
    print (a[i], end = " ")
print()

a.insert(1, 4) ### insert is used to insert one or more data elements into an array

print("Array after insertion: ", end = "") # end: is used to add any string. by default, the print functions ends with a newline. end=' 'indicates that the end character has to be identified by whitespace and not a newline.
for i in a:
    print(i, end=" ")
print()

# creating an array with double type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array

print("The new created array is: ", end=" ")
for i in range(0,3):
    print(b[i], end=" ")
print()

