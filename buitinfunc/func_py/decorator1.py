# Decorators are powerful and useful in Python since it allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

# note:
# 1. function can be treated as an object
# 2. function can be passed to another function
# 3. function can be returned inside another function

# example1. treated as an object
def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))
