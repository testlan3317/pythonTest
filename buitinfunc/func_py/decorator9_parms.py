# python decorator with parameters

def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):

        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])

        func()

    return inner

@decorator(like='geeksforit')  # - this parameter only used in the first layer of the decorator, nothing to do with the params for the real function.
def my_func():   # if needs parameters inside the my_func(), it'll need another wrapper func inside the decorator such as previous example
    print("Inside actual function")


my_func
