import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'cPWTw5c40SX6Iu9XeJuW4NIoI'
consumer_secret = 'L79cBaSIrBAV16iJcslbTuttZMYmJvZHaq24LkBKJhKS1e7yl6'
access_token = '738404396321538049-lJ9WtMNL66vsmacMOHJQ8uNdrRvZaFV'
access_token_secret = 'cH8kBtLIEdG52E1NM8EVZTeLfLUysRuB5XPmN7XMn0bQt'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
api.update_status('this tweet is uploaded using #tweepy #python')
