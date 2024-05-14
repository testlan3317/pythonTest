"""
tell() method tells you the current position within the file; in other words, the next read or write will occur at that
many bytes from the beginning of the file.

The seek(offset [, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved.

The "from" argument specifies the reference position.
- if from is 0, the beginning of the file is used as the reference position.
- if from is 1, the current position is used as the reference position.
- if from is 2, the end of file is used as the reference position.
"""

fo=open("test.txt","r+")
str=fo.read(10)
print("read String is: ", str)

#check current position
position=fo.tell()
print("current file position: ", position)

# Reposition pointer at the beginning once again
position=fo.seek(0,0)
str=fo.read(10)
print("Again read String is: ", str)
# close the file
fo.close()