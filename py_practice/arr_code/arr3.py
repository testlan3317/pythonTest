# Slicing of an array

# To print elements from beginning to a range [:index], to print elements from end use [:-index], 
# To print elements from specific index till the end [Start index:End index], 
# To print elements from end [:-index]
# To print whole array in reverse order [::-1]
# To print whole [:]

import array as arr

l = [1, 2,3,4,5,6,7,8,9,10]

a = arr.array('i', l)

print("Initial Array: ")
for i in (a):
    print(i, end = " ")

Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

Sliced_array = a[5:]
print("\nELements sliced from 5th element till the end: ")
print(Sliced_array)


Sliced_array=a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)

# index() : search for an element
print("The index of 1st occurrence of 2 is: ", end ="")
print(a.index(2))


print("The index of 1st occurrence of 1 is: ", end ="")
print(a.index(1))
