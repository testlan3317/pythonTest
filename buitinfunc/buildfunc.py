x = abs(-7.25)
print(x)

y = abs(3+5j)
print(y)

# all()
# all() returns True if all items in an iterable are true, otherwise it returns False
mylist = [ 0, 1,1]
x = all(mylist)  # return False
print(x)

mytuple = (0, True, False)
x = all(mytuple) # return False
print(x)

myset = {0, 1, 0}
x = all(myset)  # return False
print(x)

mydict = {0: "apple", 1: "orange"}
x = all(mydict) # return False, dict checks the key instead of the value.
print(x)


# any()
# returns True if any item in an iterable are true, otherwise it returns False.

print("============================")
# ascii(): returns a readable version of any object(Strings, Tuple, List, etc)
# ascii() will replace any non-ascii characters with escape characters

print(ascii(mydict))

#bin(): return binary of a number
print(bin(34))


# bytes()
# bytearray()
# chr(): returns a character from the specified unicode code. 
print(chr(97))


print("============================")
# callable(): function returns True if the specified object is callable, otherwise it returns False
def x():
    a = 5
print(callable(x)) # return true


# complex(3, 5): returns a complex number
x = complex(3, 5)
# complex(real, imaginary)



# Display the content of an object:
# dir() 
# returns all properties and methods of the specified object without the values.
class Person:
    name = "John"
    age = 36
    country = "Norway"

print(dir(Person))

print("==============vars====================")

# vars()
# returns the __dict__ attribute of an object
# __dict__ attribute is a dictionary containing the object's changeable attributes
# Note: calling the vars() function without parameter will return a dictionary containing the local symbol table
# vars(object)
# object - Any object with a __dict__ attribute
x = vars(Person)
print(x)
print("================vars end==========================")
print("================delattr()=========================")
# delattr()
# delattr() function will delete the specified attribute from the specified object.
delattr(Person, 'age')   # The Person object will no longer contain an "age" property
print(dir(Person))
print("================delattr() end=====================")

# enumerate()
# The enumerate() function takes a collection(e.g. tuple) and returns it as an enumerate object
# syntax: enumerate(iterable, start)

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
#print(list(y))
print(list(y)[0][1])

# eval()
# eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
# eval(expression, globals, locals)
# globals: Optional, A dictionary containing global parameters, locals: Optional, A dictionary containing local parameters
x = 'print(55)' # the express is coded as string
eval(x)


# exec()
# exec() function executes the specified Python code. 
# exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
# exec(object, globals, locals)
x = 'name = "John"\nprint(name)'
exec(x)

