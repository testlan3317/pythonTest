#covert wrong data Format

import pandas as pd

df = pd.read_csv('data1.csv')

df['Date'] = pd.to_datetime(df['Date'])

#print(df.to_string())


# correct the wrong data

# Set "Duration" = 45 in row 7:
df.loc[7, 'Duration'] = 45

#print(df.to_string())


# to replace wrong data for larger data sets you can create some rules.
# e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, "Duration"] = 120

print(df.to_string())


# duplicated()
# Returns True for every row that is duplicate, otherwise False
# The duplicated() method returns Boolean values for each row

print(df.duplicated())

# removing duplicates in a DataFrame
print(df.drop_duplicates())

# pandas correlation
# corr()
# calculates the relationship between each column in your data set
# df.corr()

# the number varies from -1 to 1.
#What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation. 


