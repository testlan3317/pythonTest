# load files into a DataFrame

import pandas as pd

df = pd.read_csv('data.csv')

print(df)

# A simple way to store big data sets is to use csv files(comma separated files)
# csv files contains plain text and is well know format that can be read by everyone including pandas
print(type(df))

print("======================================")
# to_string()
# could be used to print the entire DataFrame
print(df.to_string())


