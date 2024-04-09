# Destruction in Recursion
"""
In Python, you can define a destructor for a class using the __del__() method. This method is called automatically when the object is about to be destroyed by the garbage collector. Here’s an example of how to use a destructor in a recursive function:
"""

class RecursiveFunction:
	def __init__(self, n):
		self.n = n
		print("Recursive function initialized with n =", n)

	def run(self, n=None):
		if n is None:
			n = self.n
		if n <= 0:
			return
		print("Running recursive function with n =", n)
		self.run(n-1)

	def __del__(self):
		print("Recursive function object destroyed")

# Create an object of the class
obj = RecursiveFunction(5)

# Call the recursive function
obj.run()

# Destroy the object
del obj



"""
Advantages of using destructors in Python:

Automatic cleanup: Destructors provide automatic cleanup of resources used by an object when it is no longer needed. This can be especially useful in cases where resources are limited, or where failure to clean up can lead to memory leaks or other issues.

Consistent behavior: Destructors ensure that an object is properly cleaned up, regardless of how it is used or when it is destroyed. This helps to ensure consistent behavior and can help to prevent bugs and other issues.

Easy to use: Destructors are easy to implement in Python, and can be defined using the __del__() method.

Supports object-oriented programming: Destructors are an important feature of object-oriented programming, and can be used to enforce encapsulation and other principles of object-oriented design.

Helps with debugging: Destructors can be useful for debugging, as they can be used to trace the lifecycle of an object and determine when it is being destroyed.
"""
