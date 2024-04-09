# re.findall(): return all non-overlapping matches of pattern in string, as a list of strings. 
# Syntax:
# re.findall(regex,string,flag)

import re

string = """Hello my Number is 123456789 6789 and
            my friend's number is 987654321 and
            her friend's number is 123456789"""

# A sample regular expression
regex = '\d+'

match = re.findall(regex, string)
print(match)

# Regular expression is a vast topic. 
# it can do a lot of stuff. You can Match, Search, Replace, Extract a lot of data. 
# For example, below small code is powerful that it can extract email address from a text.

# new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text, re.I))  

# re.I: this flag indicate enable the case-insensitive searching.


