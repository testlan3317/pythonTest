# Creating and Using a Class
# you can model almost anything using classes. 

class Dog:
    """A simple attempt to model a dog"""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command. """
        print(f"{self.name} rolled over!")


# The __init__() method is a special method that Python runs automatically whenever we create a new instance based on the "Dog" class.
# This method has two leading underscores and two trailing underscores, a convention that helps prevent Python's default method names 
# from conflicting with your method names.  

# we define the __init__() method to have three parameters: self, name, and age.
# The self parameter is requried in the method definition, and it must come first before the other parameters. 
# It must be included in the definition because when Python calls this method later, the method call will automatically pass
# the "self" argument. 

# every method call associated with an instance automatically passes self, which is a reference to the instance itself; it 
# gives the individual instance access to the attributes and methods in the class. 

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()