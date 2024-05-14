"""
Use datetime module to get the current date and time and assign it to the filename
"""
from datetime import datetime

# get current date and time
x = datetime.now()

# create a file with date as a name day-month-year
file_name = x.strftime("%d-%m-%Y.txt")

with open(file_name, "w") as fp:
    print("create", file_name)
    pass

# with name as day-month-year-hours-minutes-seconds
file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')

with open(file_name_2,'w') as fp:
    print('create', file_name_2)

file_name_3 = r"C:\Users\Jerome\Documents\Python3.9\PythonFiles\IO" +"\\"+ x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_3, 'w') as fp:
    print('create', file_name_3)
    pass
