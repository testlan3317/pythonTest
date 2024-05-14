# Decorators with Parameters
# python functions can be treated similarly to objects.

# 1. Function can be assigned to a variable i.e. they can be referenced.
# 2. Function can be passed as an argument to another function.
# 3. Function can be returned from a function. 

"""
Syntax:
    @decorator(params)
    def func_name():
        function details

This above equivalent to 
    def func_name():
        function details

    func_name = (decorator(params))func_name(func_params)  # if func_params not none.
"""

def decorator_func(x, y):

    def inner(func):

        def wrapper(*args, **kwargs):
            print("I like food")
            print("Summation of values - {}".format(x+y))

            func(*args, **kwargs)
        return wrapper
    return inner

# Not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)

@decorator_func(12,15)
def my_fun1(*args):
    for els in args:
        print(els)

my_fun1('geeks','for','IT')

print("==============another way to call==============")

# another way of using decorators
(decorator_func(12,15))(my_fun)('geeks', 'for', "IT")
# the (my_func)('geeks', 'for', "IT") as the params -> func(*args, **kwargs) inside the wrapper. 
