# what is a Series?
# Pandas Series is like a column in a table
# it is a one-dimensional array holding data of any type.

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)  # create a series from a list

print(myvar)


# Labels:
# If nothing else is specified, the values are labelled with their index number. 

print(myvar[0])

# create your own labels:
# use index=[] 
myvar1 = pd.Series(a, index = ["x", "y", "z"])
print(myvar1)
print("====================")
# the key of dictionary becomes the label
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar2 = pd.Series(calories) # create Series object from a dictionary
print(myvar2)
print("=====================")
# to select some of items in the dictionary, use the "index" argument and specify only the items you want to include in the Series
myvar3 = pd.Series(calories, index = ["day1", "day2"])
print(myvar3)

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table. 

