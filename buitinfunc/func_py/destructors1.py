# Destructors in Python

# Destructors are called when an object gets destoryed. 
# In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically.

# The "__del__()" method is a known as a destructor method in Python.

# It is called when all references to the object have been deleted. i.e. when an object is garbage collected.

# Syntax: 
# def __del__(self):
#   body of destructor

# Note: a reference to objects is also deleted when the object goes out of reference or when the program ends.

class Employee:

    def __init__(self):
        print('Employee created')

    # Deleting (calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj

