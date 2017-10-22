from config import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET
from twitter import OAuth, TwitterStream
from pprint import pprint

stream = TwitterStream(auth=OAuth(consumer_key=CONSUMER_KEY,
              consumer_secret=CONSUMER_SECRET,
              token=TOKEN,
              token_secret=TOKEN_SECRET))


for msg in stream.statuses.filter(track="EleccionesArgentina,YaVoté,YaVote,Legislativas,Diputados,Senadores"):
  pprint(msg["text"])
