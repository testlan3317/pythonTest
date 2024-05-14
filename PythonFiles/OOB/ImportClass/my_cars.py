from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


"""
Importing an Entire Module

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

"""

"""
Improt all classes from a Module

from module_name import *

"""

# The Python Standard Library

# Python standard library is a set of modules included with every Python installation. Now that you have a basic understanding
# of how functions and classes work, you can start to use modules like these that other programmers have written. 

from random import randint
randint(1,6)