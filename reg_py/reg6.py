# re.match(): This function attempts to match pattern to whole string. 
# The re.match function returns a match object on success, None on failure. 

import re

def findMonthAndDate(string):

    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)
    print(f"type of match: {match}")
    if match == None:
        print("Not a valid date")
        return

    print("Given Data: %s" % (match.group()))
    print("Month: %s:" % (match.group(1)))
    print("Day: %s:" % (match.group(2)))


findMonthAndDate("June 24")
print("")
findMonthAndDate("I was born on June 24")


