import json

with open(input('File name: ')) as file:
    
    tweet_data = json.loads(file.read())
    
author_tw_count = {}

for tweet in tweet_data:
    
    author = tweet['author']
    
    if author not in author_tw_count:
        author_tw_count.setdefault(author,0)
        
    author_tw_count[author] += 1

sorted_tw = sorted(author_tw_count.items(),  key = lambda x: x[1],reverse=True)
max_tw = max(sorted_tw, key= lambda x: x[1])[1]

topics = set()

for tweet in tweet_data:
    
    topic = tweet['topic']
    
    if topic not in topics:
        topics.add(topic)
        
menu = int(input("input: "))

print([
    None,
    len(tweet_data),
    len(set(tweet['author'] for tweet in tweet_data)),
    '\n'.join([usr for usr, tw in sorted_tw if tw == max_tw]),
    len(topics),
    sum(map(lambda x: x['topic_priority']  == 'ALERT',tweet_data)),
    sum(map(lambda x: x['topic_priority']  == 'UNIMPORTANT',tweet_data)),
    bool(sum(map(lambda x: x['language']  != 'EN',tweet_data))),
    len(max(tweet_data, key= lambda x: len(x['text'].split()))['text'].split()),][menu])