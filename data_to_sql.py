# Load CSV to SQLite3 with Pandas
import pandas as pd
import sqlite3

# Load CSV file
data = pd.read_csv('./menu.csv')

# Connect to SQLite database
conn = sqlite3.connect('McDonalds.db')

# Save data to SQL table
data.to_sql('McDonalds_Nutrition', conn, if_exists='replace')

# Loading the data into a dataframe
df = pd.read_sql("SELECT * FROM McDonalds_Nutrition", conn)

print(df)

# Learn about the data
df.describe(include='all')

# Which food item contains the most sodium?
# Results shown in a categorical scatterplot
import matplotlib.pyplot as plt
%matplotlib inline

import seaborn as sns

plot = sns.swarmplot(x="Category", y='Sodium', data=df)
plt.setp(plot.get_xticklabels(), rotation=70)
plt.title('Sodium Content')
plt.show()

# Analyzing the data further
df['Sodium'].describe()

# Maximum value of Sodium
df['Sodium'].idxmax()

# Item with the most Sodium
df.at[df['Sodium'].idxmax(), 'Item']



