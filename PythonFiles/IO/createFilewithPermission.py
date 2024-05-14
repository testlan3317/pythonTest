"""
1.To create a file with appropriate permissions, use os.open() to create the file descriptor and set the permission.
2.open the descriptor using the built-in function open()
"""

import os
file_name_3 = r"C:\Users\Jerome\Documents\Python3.9\PythonFiles\IO\17-10-2022.txt"

# The default umask is 0o22 which turns off write permission of group and others
os.umaks(0)

with open(os.open(file_name_3, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as fp:
    fp.write('content')

"""
flags - they can be combined using the bitwise or operator |. some of them are not available on all platforms.

os.O_RDONLY - open for reading only
os.O_WRONLY - open for writing only
os.O_RDWR - open for reading and writing
os.O_NONBLOCK - do not block on open
os.O_APPEND - append on each write
os.O_CREATE - create file if it does not exist
os.O_TRUNC - truncate size to 0
os.O_EXCL - error if create and file exists
os.O_SHLOCK - atomically obtain a shared lock
os.O_DIRECT - eliminate or reduce cache effects
os.O_FSYNC - atomically obtain  an exclusive lock
os.O_NOFOLLOW - do not follow symlinks
"""

