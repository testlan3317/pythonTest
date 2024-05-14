"""
write() method writes any string to an open file, It is important to note that python strings can have binary datra and not
just text.
The write() method does not add a newline character ('\n') to the end of the string
syntax: 
fileobject.write()
"""

fo = open("test.txt", "w")
fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()
