def f1(func):
    def wrapper():
        print("Started: ")
        func()
        print("Ended")

    return wrapper

def f():
    print("Hello")

# print(f1(f))   # f1(f) actually return a function name

# f1(f)()  # call a function

f = f1(f)   # this can be replaced by decorator
f()




'''
@f1
def f():
    print("Hello")

# everytime we call f(), it's gonna call f1() and pass f as parameter   
'''