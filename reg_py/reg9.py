# re.sub()
# re.sub(pattern, repl, string, count=0, flags=0)

import re

# regular expression pattern 'ub' matches the string at "Subject" and "Uber". 
# As the case has been ignored, using Flag, 'ub' should match twice with the string upon matching, 
# 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced.

print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

# consider the case sensitivity

print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked already', count-1, flags=re.IGNORECASE))

# 'r' before the pattern denotes RE, \s is for start and end of a string.(\s: space)
print(re.sub(r'\sAND\s', '&', 'Baked Beans And Spam', flags=re.IGNORECASE))



