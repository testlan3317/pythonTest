import sys

def gen(n):
    for i in range(n):
        yield i   # loop through 5 in this case, but not include 5, and yeild i.


# do this manually
x = gen(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))


'''
for i in gen(5): 
    print(i)  # print the result that gen(n) yield

'''
