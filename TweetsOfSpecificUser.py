import tweepy
import json
import csv

# Consumer keys and access tokens, used for OAuth
consumer_key = 'cPWTw5c40SX6Iu9XeJuW4NIoI'
consumer_secret = 'L79cBaSIrBAV16iJcslbTuttZMYmJvZHaq24LkBKJhKS1e7yl6'
access_token = '738404396321538049-lJ9WtMNL66vsmacMOHJQ8uNdrRvZaFV'
access_token_secret = 'cH8kBtLIEdG52E1NM8EVZTeLfLUysRuB5XPmN7XMn0bQt'


def get_all_tweets_of(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    all_tweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    all_tweets.extend(new_tweets)
    oldest = all_tweets[-1].id-1
    i = 1
    print('loop ', i)

    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        all_tweets.extend(new_tweets)
        oldest = all_tweets[-1].id-1
        i += 1
        print('loop ', i)

    '''# create separate json files to store separate tweets
    for i, status in enumerate(last_10_tweets):
        with open("{}_last_10_tweets{}.json".format(screen_name, i+1), 'w') as f:
            json.dump(status._json, f, skipkeys=False, ensure_ascii=True, indent=4)'''
    # taking only some of information needed and storing them in a list
    separated_data = [[status.id_str, status.created_at, status.text, status.favorite_count, status.retweet_count]
                      for status in all_tweets]
    separated_data.insert(0, ['status id', 'created at', 'text', 'favourite count', 'retweet count'])

    # write data to a csv file
    with open("data.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        f.write(u'\uFEFF')
        writer.writerows(separated_data)


def main():
    get_all_tweets_of('BarackObama')

if __name__ == '__main__':
    main()
