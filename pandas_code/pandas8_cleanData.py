# Data cleaning
# means fixing bad data in your data ste
# Bad data could be:
# - Empty cells
# - Data in wrong format
# - Wrong data
# - Duplicates

# dropna()
# remove rows that contains empty cells
# return a new DataFrame, and will not change the original

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())


# if you want to change the original DataFrame, use the inplace=True argument:
df.dropna(inplace=True)
print(df.to_string())


# the dropna(inplace=True) will not return a new DataFrame, but it will remove all rows containing NULL value from the original DataFrame

# Replace Empty Values
# fillna() 
# allows us to replace empty cells with a value
df.fillna(130, inplace = True)


# Replace NULL values for specific column. e.g. "ip"
df["ip"].fillna(130, inplace = True)


# replace using Mean, Median, or Mode
# mean() - the average value( the sum of all values divided by number of values)
# median() - the value in the middle, after you have sorted all values ascending
# mode() - the value that appears most frequently

x = df["ip"].mean() 
# x = df["ip"].median()
# x = df["ip"].mode()[0]

df["ip"].fillna(x, inplace=True)


