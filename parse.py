import json
import smart_open

from pprint import pprint

with smart_open.smart_open('tweets.txt') as f:
  for i, line in enumerate(f):
    tweet = json.loads(line.decode('utf8'))
    
    try:
      print(i + 1, tweet['created_at'])
    except KeyError:
      print(tweet)
      break
    

