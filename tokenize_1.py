import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Load the CSV file into a DataFrame
df = pd.read_csv('stemmed_file.csv')

# Tokenize the tweet column and store the tokenized values in a new column
df['tokenized_tweet'] = df['tweet_without_stopwords'].apply(lambda x: word_tokenize(x))

# Tokenize the keyword column and store the tokenized values in a new column
df['tokenized_keyword'] = df['Keyword'].apply(lambda x: word_tokenize(x))

# Print the updated DataFrame
df.to_csv('final_tokenize.csv')