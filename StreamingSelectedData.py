import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener


# Consumer keys and access tokens, used for OAuth
consumer_key = 'cPWTw5c40SX6Iu9XeJuW4NIoI'
consumer_secret = 'L79cBaSIrBAV16iJcslbTuttZMYmJvZHaq24LkBKJhKS1e7yl6'
access_token = '738404396321538049-lJ9WtMNL66vsmacMOHJQ8uNdrRvZaFV'
access_token_secret = 'cH8kBtLIEdG52E1NM8EVZTeLfLUysRuB5XPmN7XMn0bQt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class MyListener(StreamListener):

    def on_data(self, raw_data):
        try:
            data = json.loads(raw_data)
            tweet = data["text"]
            username = data["user"]["screen_name"]
            line = username+' tweets: '+tweet+'\n'
            with open('TestData.txt', 'a', newline='', encoding='utf-8') as f:
                f.write(line)
            print(line)
            return True
        except:
            print('exeption occured\n\n')
            return True

    def on_error(self, status_code):
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['france'])
