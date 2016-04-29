#! /usr/local/bin/python3

import getstreamtweets
import tweetprocesser
import training
import csv
import nltk.classify
import random

enc = 'iso-8859-15'
userinput = str(input("Please give how many data you want to train: "))
model = str(input("Please give the model you want to use to train (nb or svm) : "))
classifier = training.do_training(userinput, model)[0];

tweets = []
# read test data
print('Processing tweets ...')
csvf = open('../data/test.csv', 'r', encoding=enc)
reader = csv.reader(csvf)
num_test_tweets = int(userinput)*1/4
count = 0
for row in reader:   # iterates the rows of the file in orders
    if count > num_test_tweets: break;
    else:
        count += 1
        tweet = tweetprocesser.clean_symbol(row[-1])
        if row[0] == '0': tweets.append((tweet, 'neg'))
        elif row[0] == '4': tweets.append((tweet, 'pos'))
csvf.close()

random.shuffle(tweets)
test_set = nltk.classify.apply_features(training.extract_features, tweets)
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print('Testing Accuracy is :', accuracy)
