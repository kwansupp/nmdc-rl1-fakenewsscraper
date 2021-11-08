import snscrape.modules.twitter as sntwitter
import pandas as pd

#  list to store tweet data
tweets = []

# scrape data and append to list
for i, tweet in enumberate(sntwitter.TwitterSearchScraper('fake news since:2020-03-01 until:2020-04-01').get_items()):
	print(i)
	tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username,])