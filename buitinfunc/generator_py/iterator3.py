import sys

# old way to create iterator

class Iter:
    def __init__(self, n):
        self.n = n

    # if you remove __iter__(self), the instance won't be iterable
    def __iter__(self):
        self.current = -1
        return self
    
    # if you remove __next__(self), it gets 'error iter() return non-iterator of type "Iter" '
    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        
        return self.current

x = Iter(5)
itr = iter(x)
print(itr)

print(itr)

print(itr)

'''
for i in x:
    print(i)
'''