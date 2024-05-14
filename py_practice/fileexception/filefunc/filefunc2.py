f = open("myfile.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")

# file.flush()
# cleans out the internal buffer.
# Typically means, the data will be copied from the program buffer to the operating system buffer. 
# could be understand flush() the data to the actual file.

