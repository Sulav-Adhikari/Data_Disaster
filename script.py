import snscrape.modules.twitter as sntwitter
import pandas as pd

keywords = [
    "epidemic"
    
]

# Construct the search query
query = "(from:kathmandupost) " + " OR ".join(keywords)
print(query)

tweets = set()
limit = 400

# Scrape tweets for each keyword in the list
for keyword in keywords:
    # Construct the search query for the current keyword
    query = f'"{keyword}" from:kathmandupost'
    # Scrape tweets using the search query
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) >= limit:
            break
        elif not tweet.content:
            continue
        else:
            # Append the current tweet and keyword as a tuple to the set
            tweets.add((tweet.date, tweet.username, tweet.content, keyword))

# Convert the set of tweets to a Pandas DataFrame and print it
if not tweets:
    print("No tweets found.")
else:
    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Keyword'])
    print(df)
    df.to_csv('epidemic.csv')