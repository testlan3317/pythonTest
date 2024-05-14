# Example 2: Generate-object

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))

# so a generator function returns an generator object that is iterable, i.e., can be used as an an iterators. 
