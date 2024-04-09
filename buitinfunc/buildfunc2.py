# filter()
# filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# syntax: filter(function, iterable)

ages=[5, 12, 17, 18, 24, 32]
def myFunc(x):
    if x<18:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)

# format()
# format(): formats a specified value into a specified format. 
# format(value, format)
x = format(0.5, '%')
print(x)

"""
format: -%: Percentage format   -x: Hex format, lowercase -X: Hex format, uppercase
        -n: Number format -d: decimal format -b: binary format
        ,: use a comma s a thousand separator
"""

# frozenset()
# frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable)
# frozenset(iterable)

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
#x[1] = "strawberry"  # this will cause an error, because it can't be changed.

print("=====================================")

# getattr()
# returns the value of the specified attribute from the specified object
# getattr(object, attribute, default)
# attribute - the name of the attribute you want to get the value from
# default - Optional, The value to return if the attribute does not exist

class Person:
    name = "John"
    age = 36
    country = "Norway"

x = getattr(Person, 'page', 'my message')
print(x)

# setattr()
# sets the value of the specified attribute of the specified value
# setattr(object, attribute, value)
# attribute - required. The name of attribute you want to set
# value - required 
setattr(Person, 'age', 40)
print(getattr(Person, 'age'))


# hasattr()
# returns True if the specified object has the specified attribute, otherwise False. 
# hasattr(object, attribute)

class Person:
    name = "John"
    age = 36
    country = "Norway"

x = hasattr(Person, 'age')
print(x)

# help(): Execute the built-in help system
# hex(): converts a number into a hex value

print("=======================================")
# id()
# return the id of an object. the value is the memory address of the object and will be different every time you run the program. 
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)


# isinstance()
# returns True if the specified object is of the specified type, otherwise False. 
# Note: 
# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
# isinstance(object, type)
x = isinstance(5, int)

print(x)

x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(x)

class myObj:
    name = "John"

y = myObj()

x = isinstance(y, myObj)
print(x)

# issubclass()
# returns True if the specified object is a subclass of the specified object, otherwise False
# issubclass(object, subclass)
class myAge:
    age = 36

class myObj(myAge):
    name = "John"
    age = myAge

x = issubclass(myObj, myAge)

print(x)
