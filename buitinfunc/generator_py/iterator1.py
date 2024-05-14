import sys

# iterators: an object that enables a programmer to traverse a container, paritcularly lists.
# generator: a routine that can be used to control the iteration behaviour of a loop.
# A generator is very similar to a function that returns an array.


# below is what iterator does

x = [1,2,3,4,5,6,7,8,9,10]

print(sys.getsizeof(x))  
print(sys.getsizeof(range(1,11)))

# above prove the first way to define takes more space than the 2nd way.

for element in x:
    print(element)

for i in range(1, 11):
    print(i)

y = map(lambda i: i**2, x)

print(y)
print(sys.getsizeof(y))
print(sys.getsizeof(list(y)))

# print(list(range(1,11)))

print(y.__next__()) # which is the same as the line below it.
print(next(y))


print("For Loop starts")

for i in y:
    print(i)


while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print('Done')
        break

