# iter(object, sentinel): returns an iterator object
# object - Required. An iterable object
# sentinel - Optional, if the object is a callable object the iteration will stop when the returned value is the same as the sentinel

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# reversed()
# returns a reversed iterator object
# reversed(sequence)
# sequence - required. Any iterable object
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
    print(x)


# next(): returns the next item in an iterable
# len(object): returns the number of items in an object. 
mylist = ["apple", "banana", "cherry"]
y = len(mylist)
print(y)

# map() 
# executes a specified function for each item in an iterable. The item is sent to the function as a parameter
# map(function, iterables)
# function - Required. The function to execute for each item
# iterables - Required. you can send as many iterables as you like, just make sure the function has one parameter for each iterable.

def myfunc(n):
    return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)   # print the map object
print(list(x)) # covert the map into a list, for readability

# two iterables
def myfunc1(a, b):
    return a+b

x = map(myfunc1, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

print("=======================================================")

# memoryview(): returns a memory view object from a specified object.

x = memoryview(b"Hello")
print(x)

# return the Unicode of the first character
print(x[0])

# return the Unicode of the second character 
print(x[1])

print("==============locals================")
# locals()
# returns the local symbol table as dictionary
# local symbol table: maintains all information relating to the program's local scope and is accessed in Python via locals()
x = locals()
print(x)
print(x["__file__"]) # returns /home/testuser/pythontest/venvtest/code/buitinfunc/buildfunc3.py

print("============range================")
# range()
# returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default). and stops before a specified number.
# range(start, stop, step)
# start - optional
# stop - required
# step - optional
x = range(3, 20, 2)
for n in x:
    print(n)

print("=========sort====================")

# sorted()
# returns a sorted list of the specified iterable object
# sorted(iterable, key=key, reverse=reverse)
# iterable - Required. The sequence to sort, list, dictionary, tuple etc.
# key - Optional. A Function to execute to decide the order. Default is None
# reverse - Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)

print("============slice=================")
# slice()
# slice object is used to specify how to slice a sequence. 
# slice(start, end, step)
# end - required, start, step - optional

# create a tuple and a slice object. Use the slice object to get only the two first items of the tuple.
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3) # return a slice object
print(a[x])

print("=============zip====================")
# zip() 
# returns an iterator, from two or more iterators
# zip(iterator1, iterator2, ...)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a,b) # return a zip object
print(x)
print(list(x))

print("================sum=====================")
# sum()
# returns a number, the sum of all items in an iterable.
# sum(iterable, start)
a = (1,2,3,4,5)
x = sum(a, 7) # return 22
print(x)
