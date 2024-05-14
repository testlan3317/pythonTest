import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into DataFrame object:
df = pd.DataFrame(data)
print(df)

# loc[]
# pandas use loc attribute to return one or more specified rows

print(df.loc[0]) # this returns a Pandas Series

print("======================")

# return row 0 and 1
print(df.loc[[0, 1]]) # use a list of indexes



df1 = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df1)

# locate named indexes
print(df1.loc["day2"])

