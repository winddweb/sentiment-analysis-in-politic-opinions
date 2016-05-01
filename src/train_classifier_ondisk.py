#! /usr/local/bin/python3

import pickle
import csv
import tweetprocesser
import random
import nltk.classify
from classifier import MyClassifier

number = str(input("Please give how many data you want to train: "))
model = str(input("Please give the model you want to use to train (nb or svm) : "))
classifier = MyClassifier(number, model)
classifier.train()

f = ''
# save classifier on the disk
if model == 'nb':
	f = open('../model/nb_classifier.pickle', 'wb')
elif model == 'svm':
	f = open('../model/svm_classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()

# Test against test data
tweets = tweetprocesser.label_test_tweets()
test_set = nltk.classify.apply_features(classifier.extract_features, tweets)
test_accuracy = nltk.classify.util.accuracy(getattr(classifier, 'classifier'), test_set)
print('Testing Accuracy is :', test_accuracy)