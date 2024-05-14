# Generator in Python
# Generator-Function: A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with "yield" keyword
# rather than return. If the body of a def contains yield, the function automatically becomes a generator function.

# Generator-object: Generator functions return a generator object. 
# Generator objects are used either by calling the next method on the generator or using the generator object in a "for in" loop.

# example1: Genrator-function

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)

