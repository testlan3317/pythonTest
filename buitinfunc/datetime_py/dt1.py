import datetime

# display the current date
x = datetime.datetime.now()

print(x)
print(x.year)  # output year
print(x.strftime("%A"))  # output weekday, full version. %A is the directive of strftime() 

# creating Date objects
# datetime() class of the datetime module
# datetime() class requires three parameters to create a date: year, month, day.
# datetime() also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional. 
# and has a default value of 0, (None for timezone)


x = datetime.datetime(2023, 2, 14)
print(x)

# Get unixtimestamp, we can use int(time.time_ns()/100) for python 3.7 and Up. 
# note: this way needs to import time

# convert datetime to Unix Timestamp
x = datetime.datetime.now()
print(int(x.timestamp()))


# convert timestamp to datetime
# datetime.fromtimestamp( timestamp)

# on Python version 3.2 and higher, we can use timezone class to convert Unix timestamps into other time zones. 
# from datetime import datetime, timezone
# datetime.fromtimestamp( timestamp, tz=timezone.utc)
