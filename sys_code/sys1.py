# sys module provides functions and variables used to manipulate different parts of the Python runtime environment.


# "sys.argv" : returns a list of command line arguments passed to Python script. 
# The item at index 0 in this list is always the name of the script. 
# The rest of the arguments are stored at the subsequent indices.

import sys

# test command: python sys1.py 1 2 3 
# sys.argv[0] is the script name

# sys.maxsize: returns the largest integer a variable can take. 
# sys.path: this is an environment variable that a search path for all Python modules. 

# sys.version: displays a string containing the version number of the current Python interpreter.

print(len(sys.argv))

if len(sys.argv) -1 < 3:
    print(sys.argv[0], " needs 3 parameters")
    sys.exit(-1) # error
else:
    print("You entered: ", sys.argv[1], sys.argv[2], sys.argv[3])
    sys.exit(0) # successful
"""
The optional argument arg can be an integer giving the exit status (defaulting to zero), or another type of object. If it is an integer, zero is considered “successful termination” and any nonzero value is considered “abnormal termination” by shells and the like. Most systems require it to be in the range 0–127, and produce undefined results otherwise. Some systems have a convention for assigning specific meanings to specific exit codes, but these are generally underdeveloped; Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors.
"""
