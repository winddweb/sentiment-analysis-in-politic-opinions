import tweepy
import json
from tweepy import Stream
from tweepy.streaming import StreamListener

# twitter application credentials
consumer_key = 'WKtSw7GMKsY2svfSUsMAPHxeX'
consumer_secret = 'WQCjZBoiQijGqFEHSZP3u7lzC5tDUYs5BRJpnS8sn8z91g3oan'
access_token = '713507723325808641-inJY6PB7ZAaRvcg4XEXgvcIkiq9yVmN'
access_token_secret = 'p7ilE2q6vPuz47kNvodLhGPIFirBm1PFbK6Juud0oGVEn'

tweets = []
num = 0
class listener(StreamListener):

    def __init__(self):
        super(listener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        if tweet != '':
            self.num_tweets += 1
            if self.num_tweets <= num:
                tweets.append(tweet)
                return True
            else:
                return False
        return True

    def on_error(self, status):
        print(status)

def getStreamTweets(number):
    global num
    num = number
    print('Collecting stream tweets ...')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["hillary"], languages=['en'])

    assert (len(tweets) == num)
    return tweets
