# function returns something

def hello_decorator(func):
    def inner1(*args, **kwargs): # the arguments as *args and **kwargs which means that a tuple of positional arguments or a dictionary of keyword arguments can be passed of any length.
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)

        # returning the value to the original frame
        return returned_value

    return inner1

# adding decorator to the function
@hello_decorator
def sum_two_numbers(a,b):
    print("Inside the function")
    return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a,b))


