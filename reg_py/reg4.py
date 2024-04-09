# match object has properties and methods used to retrieve info about the search, and the result:

# .span() : returns a tuple containing the start-, and end positions of the match - the index.
# .string : returns the string passed into the function
# .group() : returns the part of the string where there was a match

import re

txt = "The rain in Spain"

# match Spain \bS\w+
x = re.search(r"\bS\w+", txt)

print(x.span())

print(x.string)  # return the searched "string"

print(x.group()) # print the part of the string where there was a match.
