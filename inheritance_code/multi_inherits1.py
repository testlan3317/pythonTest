# Multiple Inheritance
# a class can be derived from more than one base class.
# all the features of the base classes are inherited into the derived class.

# python program to demonstrate

class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)

class Father:
    fathername=""
    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father: ", self.fathername)
        print("Mother: ", self.mothername)

s1 = Son()
s1.fathername="RAM"
s1.mothername="SITA"
s1.parents()
