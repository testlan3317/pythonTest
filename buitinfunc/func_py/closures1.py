# closures
# we have to understand what nested functions and non-local variables are. 

# Nested function: A function that is defined inside another function is known as a nested function.
# Nested functions are able to access variables of the enclosing scope.

# next example: define closure

def outerFunction(text):

    def innerFunction():
        print(text)

    print("11")
    innerFunction()
    print("22")

if __name__ == '__main__':
    outerFunction('Hey!')

# innerFunction() can be accessed inside the outerFunction body but not outside of its body.

