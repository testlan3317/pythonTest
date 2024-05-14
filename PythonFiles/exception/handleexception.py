"""
try:
    You do your operations here
    ...
except Exception1:
    If there is Excpetion1, then execute this block.
except Exception2:
    If there is Exception2, then execute this block.
else:
    If there is no exception then execute this block.

The code in the else block executes if the code in the try: block does not raise an exception
The else block is a good place for code that does not need the try: block's protection.
"""


try:
    fh = open("testfile",'w')
    fh.write("This is my test file for exception handling!!!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

"""
You can also use the except statement with no exceptions defined as follows:
try:
    you do your operation here
    ...
except:
    If there is any exception, then execute this block
    ...
else:
    If there is no exception then execute this block

This kind of try-except statement catches all the exceptions that occur. Using this kind of try-except statement is not
considered a good programming practice though, because it catches all exceptions but does not make the programmer identify
the root cause of the problem.
"""

"""
you can also use the same except statement to handle multiple exceptions as follows:
try:
    You do your operations here
    ...
except(Exception1 [, Exception2])
    if there is any exception from the given exception list, 
    then execute this block.
    .....
else:
    If there is no exception then execute this block.
"""

"""
The try-finally clause:
You can use a finally block along with a try block. The finally block is a place to put any code that must execute, 
whether the try block raised an exception or not. The syntax of the try-finally statement is

try:
    You do your operations here
    ....
    Due to any exception, this may be skipped
finally:
    this would always be executed
    .....
"""

try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can\'t find file or read data")
    
"""
Argument of an Exception
An exception can have an argument, which is a value that gives additional information about the problem.
try:
    You do your operation here
    ....
except ExceptionType as Argument
    You can print value of Argument here...
    
This variable receives the value of the exception mostly containing the cause of the exception. The variable can 
receive a single value or multiple values in the form of a tuple. This tuple usually contains the error string, 
the error number, and an error location.
"""

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument doesnot contain numbers\n", Argument)

# call above function here
temp_convert("xyz")


"""
Raising an Exception:
Syntax:
raise [Exception [, args [, traceback]]]

Here, Exception is the type of exception (for example, NameError) and argument is a value for the exception argument.
The argument is optional; if not supplied, argument is None
traceback, is also optional(rarely used in practice), and if present, is the traceback object used for the exception

Note:
In order to catch an exception, an "except" clause must refer to the same exception thrown either as a class object
or a simple string.

"""
def functionName (level):
    if level < 1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level

try:
    l = functionName(-10)
    print("level = ", l)
except Exception as e:
    print("error in level argument", e.args[0])
