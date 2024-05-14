# cp -r `ls -A | grep -v "dir2"` /home/sk/backup/

# readline()
# file.readline(size)
# size - optional. The number of bytes from the line to return. Default -1, which means the whole line

f = open("demofiles.txt", "r")
print(f.readline().rstrip())
print(f.readline(7).strip())
print(f.readline())
f.close()
