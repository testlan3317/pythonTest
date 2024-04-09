# re.search(): better used to test the regular expression other than extracting

# re.search(): This method either returns None (if the patter doesn't match), or a re.MatchObject that contains information about the matching part of the string.
# This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. 

import re

regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 25")
print(f"type of match: {match}")
if match != None:

    # This will print [14, 21), since it matches at index 14 and ends at 21. 
    print ("Match at index %s, %s" % (match.start(), match.end()))  #match.start() : start index. match.end(): end index.
    
    # we use group() method to get all the matches and captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ..return the capture groups in order.(from left to right)
    # match.group() equivalent to match.group(0)
    
    # so this will print "June 24"
    print("Full match: %s" % (match.group(0)))
    
    # this will print "June"
    print("Month: %s:" % (match.group(1)))

    # this will print "24"
    print("Days: %s:" % (match.group(2)))
else:
    print("The regex pattern does not match.")
