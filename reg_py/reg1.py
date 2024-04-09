# regular expression : a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern. 

# Python has a built-in package called "re", which can be used to work with Regular Expressions.


import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$",txt)
print(x)

if x:
    print("Matched")
else:
    print("No match")
