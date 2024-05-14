# Pandas Plotting
# plot()
# use Pyplot, a submodule of the Matplotlib library to visulize the diagram on the screen

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data1.csv')

df.plot()

plt.show()


# Scatter Plot
# A scatter plot needs an x- and y-axis
# kind = 'scatter'
df.plot(kind = 'scatter', x='Duration', y='Calories')
plt.show()


"""
Remember: In the previous example, we learned that the correlation between "Duration" and "Calories" was 0.922721, and we concluded with the fact that higher duration means more calories burned.

By looking at the scatterplot, I will agree.
"""

# Histogram
# use kind = 'hist'
# histogram needs only one column
# A histogram shows us the frequency of each interval. e.g. how many workouts lasted between 50 and 60 minutes?

df["Duration"].plot(kind='hist')
plt.show()

