import pandas as pd

file = 'tweets_oct2018'

# read json as df
json = file + '.json'
print("reading json file...")
df = pd.read_json(json, lines=True)

# filter df to contain only direct "fake news" phrases
print("filtering 'fake news' phrase...")
df = df[df['content'].str.contains("fake news")]

# print(list(df))
print("getting top retweets and likes...")
# get tweets with top 5 retweet
df_top_rt = df.sort_values(by=['retweetCount'],ascending=False).head(10)
# print(df_top_rt['retweetCount'])

# get tweets with top 5 likes
df_top_likes = df.sort_values(by=['likeCount'],ascending=False).head(10)

print("saving to file...")
# save results to file
csv_rt = file + '_top10_rts.csv'
# xls_rt = file + '_top10_rts.xlsx'
csv_likes = file + '_top10_likes.csv'
# xls_likes = file + '_top10_likes.xlsx'

df_top_rt.to_csv(csv_rt)
df_top_likes.to_csv(csv_likes)

# df_top_rt.to_excel(xls_rt)
# df_top_likes.to_excel(xls_likes)