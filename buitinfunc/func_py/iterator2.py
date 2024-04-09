# creating and looping over an iterator using iter() and next()


# example: iterates from 10 to given value
class Test:

    # constructor
    def __init__(self, limit):
        self.limit = limit
    
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. 
    def __next__(self):
        x = self.x
        
        # stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
        self.x = x + 1
        return x

# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)
