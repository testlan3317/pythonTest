# File Handling
# open()
# open(filename, mode)
# mode: r - read(Default value) error if the file doesn't exist
#       a - append, create file if it doesn't exist
#       w - open file for writing, creates file if it doesn't exist
#       x - create - creates the specified file, returns error if the file exists.

# in addition you can specify if the file should be handled as binary or text mode
#       t - Text(Default value) text mode
#       b - Binary mode (e.g. images)

f = open("demofiles.txt") # it equals open("demofile", "rt")
print(f.read())
f.close()

f = open("demofiles.txt", "r")
# By default the read() method returns the whole text, but you can also specify how many characters you want to return
print(f.read(5))
