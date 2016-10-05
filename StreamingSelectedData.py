import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from Key import *

class MyListener(StreamListener):

    def on_data(self, raw_data):
        global tweet_number
        try:
            '''
            This function gets the streaming data about the filtering objects.
            This function can be modified to insert data on preferred database.
            '''
            data = json.loads(raw_data)
            tweet = data["text"]
            username = data["user"]["screen_name"]
            hashtag = data['entities']['hashtags']
            hasht = []
            for item in hashtag:
                hasht.append(item['text'])
            line = username+' tweets:: '+tweet+'\n'
            with open('TestData.txt', 'a', encoding='utf-8') as f:
                f.write(line)
            print(tweet_number, end=" ")
            tweet_number += 1
            print(hasht, end= " ")
            print(line)
            return True
        except:
            print('exception occurred\n\n')       # debug to test if on_data() working or not
            return True

    def on_error(self, status_code):
        return True



def main():
    track_list = [str(x) for x in input("enter topics about you want to do a Sentiment analysis : ").split()]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=track_list)     # filter can be modified to get necessary data

if __name__ == '__main__':
    main()
