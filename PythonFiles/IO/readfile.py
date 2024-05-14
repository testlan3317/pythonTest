"""
read() method reads a string from an open file. It is important to note that Python strings can have binary
data apart from text data.
syntax:
fileobject.read([count])

passed parameter is the number of bytes to read from the opened file. This method starts reading from the beginning of the file
and if count is missing, then it tries to read as much as possible, maybe untill the end of file.
"""

fo = open("test.txt", "r+")
str = fo.read(10)
print(f"Read String is: {str}")
