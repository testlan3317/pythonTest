# Supporting the "with" statement in user defined objects
# the same functionality can be provided in user defined objects. 
# supporting with statement in your objects will ensure that you never leave any resource open.

# Note:
# to use with statement in user defined objects you only need to add the methods: __enter__() and __exit__() in the object methods. 

# example

class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):        # this will executed as soon as the execution enters the context of the "with" block.
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, *args):  # this will executed after the methods executed inside the "with" block.
        self.file.close()

# using with statement with MessageWriter
with MessageWriter('my_file.txt') as xfile:  # The name xfile here is used to refer to the file descriptor returned by __enter__().
    xfile.write('Hello world')

"""
what are resource descriptors?
These are the handles provided by the operating system to access the requested resources. 


This is how we use the with statement with user defined objects. 
This interface of __enter__() and __exit__() methods which provides the support of with statement is called Context Manager.
"""
