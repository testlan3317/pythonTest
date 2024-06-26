# Polymorphism with inheritance
"""
In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class.
"""
class Bird:
def intro(self):
	print("There are many types of birds.")

def flight(self):
	print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
def flight(self):
	print("Sparrows can fly.")

class ostrich(Bird):
def flight(self):
	print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

