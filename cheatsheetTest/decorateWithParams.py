'''
A decorator with arguments is a decorator that accepts parameters to customize its behavior. 
It requires an extra layer of nesting because the arguments are passed to an outer function that returns the actual decorator.

Basic Structure:
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            # Use arg1, arg2 here to customize behavior
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
    
'''

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}!")

greet("JACKY")

