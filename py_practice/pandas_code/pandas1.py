# Pandas is a Python libaray used for working with data set
# it has functions for analyzing, cleaning, exploring, and manipulating data.
# why use Pandas?
# pandas can clean messy data sets, and make them readable and relevant
# pandas allows us to analyze big data and make conclusions based on statistical theories.

import pandas as pd

#key - title column
# Date sets in Pandas are usually multi-dimensional tables, called DataFrames. 
# Series is like a column, a DataFrame is the whole table

# records number is the nubmers of items
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print(pd.__version__)

for (index, row) in myvar.iterrows():
    print(row.cars)