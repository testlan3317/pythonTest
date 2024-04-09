"""
In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
Syntax:

@gfg_decorator
def hello_decorator():
    print('Gfg')
"""
"""
Above code is equivalent to 
def hello_decorator():
    print('Gfg')

hello_decorator = gfg_decorator(hello_decorator)
"""



# defining a decorator
def hello_decorator(func):
    # inner is a wrapper function, in which the argument is called
    def inner():
        print("Hello, this is before function execution")

        # calling the actual function now inside the wrapper function.
        func()
        
        print("This is after function execution")
    return inner

# defining a function, to be invoked inside wrapper
def function_to_be_used():
    print("This is inside the function !!")

# passing 'function_to_be_used' inside the decorator 
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()
