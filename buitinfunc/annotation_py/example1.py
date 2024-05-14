import time

def before_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("End")

    return wrapper

class Test:
    @before_after
    def decorate_method(self):
        print("run")

t = Test()
t.decorate_method()