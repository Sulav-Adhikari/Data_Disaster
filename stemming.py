import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download stopwords and punkt tokenizer if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Read the CSV file
df = pd.read_csv('final_stopword_removed.csv')



# Remove stopwords from the "tweet_lowercase" column
stopwords_set = set(stopwords.words('english'))

df['tweet_without_stopwords'] = df['tweet_lowercase'].apply(lambda x: ' '.join([word for word in word_tokenize(x) if word not in stopwords_set]))

# Apply stemming to the "tweet_without_stopwords" column
stemmer = PorterStemmer()

df['tweet_stemmed'] = df['tweet_without_stopwords'].apply(lambda x: ' '.join([stemmer.stem(word) for word in word_tokenize(x)]))

# Save the updated DataFrame to a new CSV file
df.to_csv('stemmed_file.csv', index=False)
