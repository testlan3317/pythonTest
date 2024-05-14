"""
create a file with built-in open() method
syntax:
open("file_path","access_mode")

w: create a new file for writing. If a file already existing, it truncates the file first. 
   Use to create and write content into a new file.

x: Open a file only for exclusive creation. If the file already exists, this operation fails.

a: Open a file in the append mode and add new content at the end of the file.

b: Create a binary file

t: Create and open a file in a text mode. 
"""

import os 

fp = open("test.txt", "w")

fp.write("First line###")

fp.close()

"""
verify the result using:
os.listdir(directory_path) function to list all files from a folder before and after creating a file.

Use "os.path.isfile(file_path)" function to verify if a newly created file exists in a directory.

"""
print(os.listdir())

# verify file exists
print(os.path.isfile("test.txt"))

"""
create File in A Specific Directory:
To create a file inside a specific directory, we need to open a file using the absolute path. 

r'...' string modifier causes the '...' string to be interpreted literally. That means, r'My\Path\Without\Escaping' will 
evaluate to 'My\Path\Without\Escaping' - without causing the backslash to escapse characters. 
The path is equivalent to 'My\\Path\\Without\\Escaping'
"""
with open(r'C:\Users\Jerome\Documents\Python3.9\PythonFiles\IO\testingfile.txt', 'w') as fp:
    fp.write("This is the first line....Testing")
    pass

"""
Note: Using the with statement a file is closed automatically it ensures that all the resources that are tied up with the
file are released.
"""

path = r"C:\Users\Jerome\Documents\Python3.9\PythonFiles\IO"
file_name = "testingfile1.txt"
file_path = path+"\\"+file_name
print(file_path)
if os.path.exists(file_path):
    print('file already exists')
else:
    with open(os.path.join(path, file_name), 'w') as fp:
        fp.write("This is a new line in testing file 1")
        pass

"""
Argument of an Exception
An exception can have an argument, which is a value that gives additional information about the problem.
try:
    you do your operation here.
    ...
except ExceptionType as Argument:
    You can print value of Argument here...

This variable receives the value of the exception mostly containing the cause of the exception. The variable can receive
a single value or multiple values in the form of a tuple.

Note:
This tuple usually contains the error string, the error number, and an error location.
"""

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers \n", Argument)

# call above function here.
temp_convert("xyz")

"""
Raising an Exception:
You can raise exception in several ways by the raise statement. The general syntax for the raise statement is as follows
syntax:
    raise [Exception [, args [, traceback]]]

argument is avalue for the exception argument (optional), if not supplied, the exception argument is None.
traceback is also optional (and rarely used in practice), and if present, is the traceback object used for the exception.

Note: in order to catch an exception, an except clause must refer to the same exception thrown either as a class object
or a simple string.

"""

def functionName(level):
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
