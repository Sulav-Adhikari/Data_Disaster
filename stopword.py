import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Read the CSV file
df = pd.read_csv('final1.csv')

# Convert the "tweet" column to lowercase
#df['tweet_lowercase'] = df['tweet'].str.lower()

# Remove stopwords from the "tweet_lowercase" column
stopwords_set = set(stopwords.words('english'))

df['tweet_without_stopwords'] = df['tweet_lowercase'].apply(lambda x: ' '.join([word for word in word_tokenize(x) if word not in stopwords_set]))

# Save the updated DataFrame to a new CSV file
df.to_csv('final_stopword_removed.csv', index=False)
