"""
Python "os" module provides methods that help you perform file-processing operations, such as renaming and deleting files.
Syntax:
os.rename("oldname", "newname")
"""

import os

# rename a file
os.rename("test.txt", "python_test_txt.txt")
# delete a file
os.remove("python_test_txt.txt")