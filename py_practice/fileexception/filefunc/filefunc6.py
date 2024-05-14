# seek() : sets the current file position in a file system
# file.seek(offset)

f = open("demofiles.txt", "r")
print(f.seek(4)) # return the new position 4
print(f.readline())
