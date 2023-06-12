import pandas as pd

# Read the CSV file
df = pd.read_csv('final.csv')

# Convert the "tweet" column to lowercase
df['tweet_lowercase'] = df['Tweet'].str.lower()

# Save the updated DataFrame to a new CSV file
df.to_csv('final1.csv', index=False)
