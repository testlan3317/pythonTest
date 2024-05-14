# Verbose in Python Regex
# re.VERBOSE: This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate
# logical sections of the pattern and add comments. 

# whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped backslash, or within tokens
# like *?, 

# without using verbose

import re

regex_email = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$', re.IGNORECASE)
objtype = type(regex_email)
print(f"re.compile returns type is {objtype}")
# Using Verbose
regex_email1 = re.compile(r"""
        ^([a-z0-9_\.-]+)         # local Part
        @                        # single @ sign
        ([0-9a-z\.-]+)           # Domain name
        \.                       # single Dot .
        ([a-z]{2,6})$            # Top level Domain
        """, re.VERBOSE | re.IGNORECASE)

# re.compile(): returns a RegexObject which is then matched with the given string.
# re.rempile() returns a pattern objects, which have methods for various operations such as search for a pattern matches or performing string substitutions.

# re.split(): returns a list. 
# syntax: re.split(pattern, string, maxsplit=0, flags=0)
# maxsplit if not provided is considered to be 0
# if any nonzero value is provided, then at most that many splits occur. 

# re.sub(): find the match, replace with repl, count control the replacement times. 
# syntax: re.sub(pattern, repl, string, count=0, flags=0)


email = "exceptopatronum@gmail.com"

res = regex_email1.fullmatch(email)  # using fullmatch function. returns a MatchObject Instance
print(res.group())
print(res.group(1))
print(res.group(2))
print(res.group(3))
