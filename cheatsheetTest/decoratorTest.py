# A decorator in its simplest form is a function that takes another function as an argument and returns a wrapper

def your_decorator(func):
    def wrapper():
        # Do stuff before func...
        print('Before func')
        func()
        # Do stuff after func...
        print('After func')
    return wrapper

@your_decorator
def foo():
    print("hello world decorator")

foo()

# decorator for a function with parameters
def your_decorator1(func):
    def wrapper(*args, **kwargs):
        # do stuff before func...
        print('Before func')
        # do stuff after func...
        func(*args, **kwargs)
        print('After func')
    return wrapper

@your_decorator1
def foo1(bar):
    print("My name is " + bar)

foo1("Jacky")

