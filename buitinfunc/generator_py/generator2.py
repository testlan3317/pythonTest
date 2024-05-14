import sys

# generator: yield method needed.

def gen():
    yield 1
    print('Pause 1')
    yield 2
    print('Pause 2')
    yield 3
    print('Pause 3')
    yield 4
    print('Pause 4')

x = gen()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# The point of using Generator is when you loop through a sequence or a large amount of data without
# needing to store all of it

# when you use generator, you do not care about the data before or after iteration. you only care about
# the current piece of data that you're looking at.

