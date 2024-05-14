import sys

x = range(1,11)  # return range object

print(x)

# in order to get an iterator, there is a function called iter() or .__iter__()

print(next(iter(x)))