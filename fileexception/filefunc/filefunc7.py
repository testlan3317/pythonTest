# tell(): returns the current file position in a file system
# file.tell()
f = open("demofiles.txt", "r")
print(f.tell())   # initial position is 0

print(f.readline().rstrip())
print(f.tell())



# truncate(): resizes the file to given size of bytes
# file.truncate(size)
