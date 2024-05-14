"""
syntax:
open("filename", "open_mode", buff)
"""
fo = open("test.txt", "wb")
print(f"Name of the file: {fo.name}")
print(f"Closed or not: {fo.closed}")
print(f"Opening mode: {fo.mode}")
fo.close()
"""
The close() method of a file object flushes any unwritten information and closes the file object, 
after which no more writing can be done.
syntax:
fileobject.close()
"""

