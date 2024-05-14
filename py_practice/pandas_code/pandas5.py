import pandas as pd

df = pd.read_csv('data.csv')

print(df)

# check the number of maximum returned rows
# my system the number is 60, which means if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

print(pd.options.display.max_rows)
