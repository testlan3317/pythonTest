# How does the operator overloading actually work?
# Whenever you change the behavior of the existing operator through operator overloading, you have to redfeine the special function
# that is invoked automatically when the operator is used with the objects.

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2))
print(A.__add__(ob3,ob4))
#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))

"""
Here, We defined the special function “__add__( )”  and when the objects ob1 and ob2 are coded as “ob1 + ob2“, the special function is automatically called as ob1.__add__(ob2) which simply means that ob1 calls the __add__( ) function with ob2 as an Argument and It actually means A .__add__(ob1, ob2). Hence, when the Binary operator is overloaded, the object before the operator calls the respective function with object after operator as parameter
"""


