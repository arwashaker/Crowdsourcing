# The usual preamble
import pandas as pd
import matplotlib.pyplot as plt

# Make the graphs a bit prettier, and bigger




broken_df = pd.read_csv('C:/Users/Arwa/Desktop/Freelancers_Data_final.csv')
# Look at the first 3 rows
print(broken_df[:3])
# Selecting  a column
print(broken_df['name'])
# Plotting a column
broken_df['rating'].plot()
plt.draw()
# what s the most rating the worker has being given
print(broken_df['rating'].value_counts())
broken_df['rating'].value_counts().plot(kind='bar')
