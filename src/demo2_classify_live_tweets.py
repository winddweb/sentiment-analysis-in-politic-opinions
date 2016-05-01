#! /usr/local/bin/python3

import getstreamtweets
import tweetprocesser
import pickle
from classifier import MyClassifier

# read trained classifier from disk
f = ''
model = str(input("Please give the model you want to use (nb or svm) : "))
if model == 'nb':
	f = open('../model/nb_classifier.pickle', 'rb')
elif model == 'svm':
	f = open('../model/svm_classifier.pickle', 'rb')
my_classifier = pickle.load(f)
classifier = getattr(my_classifier, 'classifier')
f.close()

# test with real time tweets
num_tweets = str(input("Please give how many real time tweets you want to collect: "))
live_tweets = getstreamtweets.getStreamTweets(int(num_tweets))
print('Classify the tweets ...')
print('========================================')
for t in live_tweets:
    tweet = tweetprocesser.clean_symbol(t)
    print( t + ' => ' + classifier.classify(my_classifier.extract_features(tweet)))