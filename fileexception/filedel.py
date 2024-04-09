# delete a file you must import OS module and run its os.remove() function
# delete file:  os.remove("filename")
# delete folder: os.rmdir("folder")

import os


if os.path.exists("demofiles1.txt"):
    os.remove("demofiles1.txt")
    print("file deleted")
else:
    print("The file doesn't exist")

