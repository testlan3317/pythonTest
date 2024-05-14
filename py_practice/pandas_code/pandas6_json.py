# Read JSON
# Big data sets are often stored, or extracted as JSON

import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())
