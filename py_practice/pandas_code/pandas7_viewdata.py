# Viewing Data
# head()
# returns the headers and a specified number of rows, starting from the top

import pandas as pd

df = pd.read_csv('data.csv')

# if the number of row is not specified, the head() method will return top 5 rows
print(df.head(10))

print(df.head())


# tail() returns the headers and a specified number of rows, starting from the bottom. default 5 rows
print(df.tail())


# info()
# gives you more information about the data set
print(df.info())
