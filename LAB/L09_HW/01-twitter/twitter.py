import json

with open(input('File name: ')) as file:
    
    tweet_data = json.loads(file.read())




        
menu = int(input("input: "))


_1 = lambda: len(tweet_data)
_2 = lambda: len(set(tweet['author'] for tweet in tweet_data))

def _3():

    author_tw_count = {}

    for tweet in tweet_data:
        
        author = tweet['author']
        
        if author not in author_tw_count:
            author_tw_count.setdefault(author,0)
            
        author_tw_count[author] += 1

    sorted_tw = sorted(author_tw_count.items(),  key = lambda x: x[1],reverse=True)
    max_tw = max(sorted_tw, key= lambda x: x[1])[1]
    
    return '\n'.join([usr for usr, tw in sorted_tw if tw == max_tw])

def _4():
    topics = set()

    for tweet in tweet_data:
        
        topic = tweet['topic']
        
        if topic not in topics:
            topics.add(topic)
            
    return len(topics)

_5 = lambda: sum(map(lambda x: x['topic_priority']  == 'ALERT',tweet_data))
_6 = lambda: sum(map(lambda x: x['topic_priority']  == 'UNIMPORTANT',tweet_data))
_7 = lambda: bool(sum(map(lambda x: x['language']  != 'EN',tweet_data)))
_8 = lambda: len(max(tweet_data, key= lambda x: len(x['text'].split()))['text'].split())

print([_1, _2, _3, _4, _5, _6, _7, _8][menu]())