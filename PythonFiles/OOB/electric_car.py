# inheritance
# when you are writing an new class based on an existing class, you'll often want to call the __init__() method
# from the parent class. This will initialize any attributes that were defined in the parent __init__() method and make them
# available in the child class.

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles



# You can override any method from the parent class that doesn't fit what you're trying to model with the child class.
# To do this, you define a method in the child class with the same name as the method you want to override in the parent
# class.


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")

# Instances as Attributes
# When modeling something from the real world in code, you may find that you're adding more and more detail to a class. 
# you'll find that you have a growing list of attributes and methods and that your files are becoming lengthy. 
# In this situations, you might recognize that part of one class can be written as a separate class. 
# You can break your large class into smaller classes that work together. 

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


# Importing Classes
# You'll want to keep your files as uncluttered as possible. To help, Python lets you store classes in modules and then
# import the classes you need into yuour main program.

