# "re" module offers a set of functions that allows us to search a string for a match

# findall:  returns a list containing all matches
# search :  returns a Match object if there is a match anywhere in the string
# split  :  returns a list where the string has been split at each match
# sub    :  replaces one or many matches with a string

import re

txt = "That will be 59 dollars"

# Find all digit characters:

x = re.findall("\d", txt)

print(x)

x = re.findall("[a-m]", txt)
print(x)


# *  : zero or more occurences of previous obj
# +  : one or more occurences of previous ojb

# ?  : zero or one occurence of previous obj

# {} : exactly the specified number of occurences


# () : capture and group

