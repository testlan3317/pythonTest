# example 3, return function inside another function.

def create_adder(x):
    
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)  # 15 for outer function.
print(add_15(10)) # 10 for inner function "adder(y)"
