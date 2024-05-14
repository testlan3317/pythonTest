# constructor
# creating and initializing objects of a given class is a fundamental step in oob programming. 
# This step referred to as object construction or instantiation. 

# Python's Instantiation Process
# you trigger Python's instantiation process whenever you call a Python class to create a new instance. This process runs through 2 separate steps
# 1. Creat a new instance of the taget class
# 2. Initialize the new instance with an appopriate initial state.

# Python classes have a special method called .__new__(), which is responsible for creating and returning a new empty object. 
# Then another special method .__init__(), takes the resulting object, along with the class constructor's arguments.


# note: calling a class isn't the same as calling an instance of a class. 
# These are two different and unrelated topics.
# To make a class's instance callable, you need to implement a .__call__() special method, which has nothing to do with Python's instantiation process.

class Point:
    x, y = 0, 0
    def __new__(cls, *args, **kwargs):   # cls: means class. it's python's convention. takes class as its first arguments
        print("1. create a new instance of Point.")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y
                
    def __repr__(self) -> str:
        #return "x is {x}, and y is {y}".format(self.x,self.y)
        return f"{type(self).__name__}(x={self.x}, y={self.y})"


if __name__ == '__main__':
    obj1 = Point(4,5)
    obj2 = Point(10,20)   
    print(obj1)
    print(obj2)
