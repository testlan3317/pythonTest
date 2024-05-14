# A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

def outerFunction(text):

    def innerFunction():
        print(text)


    return innerFunction

if __name__ == '__main__':

    myFunction = outerFunction('Hey!~')
    myFunction()

# The function innerFunction has its scope only inside the outerFunction. But with the use of closure, we can easily extended its scope to invoke a function
# outside its scope


