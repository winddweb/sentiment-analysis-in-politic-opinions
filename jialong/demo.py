#! /usr/local/bin/python3

import getstreamtweets
import tweetprocesser
import training

userinput = str(input("Please give how many data you want to train: "))
model = str(input("Please give the model you want to use to train (nb or svm) : "))
classifier = training.do_training(userinput, model)[0];
# test with real time tweets
num_tweets = str(input("Please give how many real time tweets you want to collect: "))
live_tweets = getstreamtweets.getStreamTweets(int(num_tweets))
for t in live_tweets:
    tweet = tweetprocesser.clean_symbol(t)
    print( t + ' => ' + classifier.classify(training.extract_features(tweet)))