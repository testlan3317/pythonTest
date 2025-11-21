'''
why we need 

We need functools.wraps to preserve the original function's metadata because decorators inherently replace the 
original function with the wrapper function, causing loss of important information.

If there is no meta data preserve, it'll lose some information

def my_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def original_function():
    """This is the original function's docstring"""
    pass

# Let's check what happens:
print(original_function.__name__)     # Output: 'wrapper'
print(original_function.__doc__)      # Output: 'Wrapper docstring'

'''
# if we have metadata preserved

from functools import wraps

def my_decorator(func):
    @wraps(func)  # This preserves the original function's metadata
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def original_function():
    """This is the original function's docstring"""
    pass

# Now metadata is preserved:
print(original_function.__name__)     # Output: 'original_function'
print(original_function.__doc__)      # Output: 'This is the original function's docstring'
