# Providing Custom Object creators
"""
Typically, you'll write a custom implementation of .__new__() only when you need to control the creation of a new instance at a low level.
Now, if you need a custom implementation of this method, then you should follow a few steps:
    1. create a new instance: by calling super().__new__() with appropriate arguments
    2. customize the new instance: according to your specific needs
    3. return the new instance: to continue the instantiation process.
"""

class SomeClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  # create a new instance and allocate memory for it. to access the parent class's.__new__() method, use super()
        # it's important to know that object.__new__() itself only accepts a single argument. <-- the parent is object
        
        # however, object.__new__() still accept and passes over extra arguments to .__init__() if you doesn't overwrite the .__new__() from the object(top level, e.g. you didn't inherit any class)
        """
        This could be explained in --> subclassing Immutable Built-in Types. (overwrite .__new__())
        for example class Distance(float):
        class Distance(float):
            def __new__(cls, value, unit):
                instance = super().__new__(cls, value)
                instance.unit = unit
                return instance
        check the next example constructor3.py for testing
        """
       
        # customize your instance from here...
        
        print("1")
        print("2")

        return instance
