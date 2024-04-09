# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below:

# \A  : returns a match if the specified characters are at the beginning of the string. "\AThe"
# \b  : returns a match if the specified characters are at the beginning or at the end of a word r"\bain" , r"ain\b"
# \B  : returns a match where the specified characters are present, but Not at the beginning (or at the end) of a word r"\Bain",  r"ain\B"


# \s  : returns a match where the string contains a white space character
# \S  : returns a match where the string does not contain a white space character

# \d  : returns a match where the string contains digits (numbers from 0-9)
# \D  : returns a match where the string does not contain digits
# \w  : returns a match where the string contains any word characters(characters from a to Z, digits from 0-9, and the underscore _ character
# \W  : returns a match where the string does not contain any word characters
# \Z  : returns a match if the specified characters are at the end of string    "Spain\Z"

import re

txt = "The rain in Spain"

# check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x)

if (x):
    print("matched")
else:
    print("no match")


x = re.search("\s", txt)   #note: if no match, return None
print("The first white-space character is located in position: ", x.start())

# split()
x = re.split("\s", txt)
print(x)

# sub() : replaces the matches with the text of your choice:

x = re.sub("\s", "9", txt)
print(x)

# sub() can also specify the number of replacements by specify the "count" parameter
x = re.sub("\s", "9", txt, 2)  # replace 2
print(x)


