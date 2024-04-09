import os

parent_dir = "/home/testuser/pythontest/venvtest/code/os_code/"
directory = "dirtest1"

# Path
path = os.path.join(parent_dir, directory)

print(path)

#os.mkdir(path)  # create the directory
mode = 0o777   #0o means: Octal

os.mkdir(path, mode) # create directory with mode

#mkdirs(): can go against the parent and current directory if they are not exists

# os.chdir("../")

# os.path.getsize(): python will give us the size of the file in bytes. we need to pass the name of the file as a parameter.
# os.remove() : remove a file in our system. we need to pass the name of the file as a parameter
# os.close() : close file descriptor. 
# A file opened using open(), can be closed by close()only. 
# But file opened through os.popen(), can be closed with close() or os.close(). If we try closing a file opened with open(), using os.close(), Python would throw TypeError

# os.close(file)

# os.popen(command[, mode [, bufsize]])
# This method opens a pipe to or from command. The return value can be read or written depending on whether the mode is 'r' or 'w'
