"""
User-Defined Exceptions:
Here is an example related to RuntimeError. Here, a class is created that is subclassed from RuntimeErorr. 
This is useful when you need to display more specific information when an exception is caught.

"""

class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

"""
once you have defined the above class,  you can raise the exception as follows
"""
try:
    raise NetworkError("Bad hostname")
except NetworkError as e:
    print (e.args)