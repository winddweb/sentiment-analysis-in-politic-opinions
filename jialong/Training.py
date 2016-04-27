#! /usr/local/bin/python3

import csv
import nltk
import re
import time
import nltk.classify
import getstreamtweets
import tweetprocesser
from random import shuffle
from nltk.classify import apply_features
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    return wordlist.keys()

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def do_training(userinput):
    trainingRow = int(userinput) / 2
    firstNegRow = 0
    firstPosRow = 800000
    # total positive tweets training set : 248,576
    enc = 'iso-8859-15'
    pos_tweets = []
    neg_tweets = []
    rowNum = 0
    print('Processing tweets ...')
    # read csv training set
    csvf = open('../dataset/training.csv', 'r', encoding=enc)
    reader = csv.reader(csvf)
    for row in reader:   # iterates the rows of the file in orders
        if rowNum < firstNegRow + trainingRow:
            tweet = tweetprocesser.clean_symbol(row[-1])
            neg_tweets.append((tweet, 'neg'))
            rowNum += 1
        else:
            if rowNum < firstPosRow: rowNum += 1
            elif rowNum < firstPosRow + trainingRow:
                tweet = tweetprocesser.clean_symbol(row[-1])
                pos_tweets.append((tweet, 'pos'))
                rowNum += 1
            else:
                break

    csvf.close()
    # test data/training data should be 1 : 4
    negcutoff = int(len(neg_tweets)*4/5)
    poscutoff = int(len(pos_tweets)*4/5)
    tweets = neg_tweets + pos_tweets
    training_list = neg_tweets[:negcutoff] + pos_tweets[:poscutoff]
    test_list = neg_tweets[negcutoff:] + pos_tweets[poscutoff:]
    # shuffle data
    shuffle(tweets)
    shuffle(training_list)
    shuffle(test_list)
    global word_features
    word_features = get_word_features(get_words_in_tweets(tweets))
    training_set = nltk.classify.apply_features(extract_features, training_list)
    test_set = nltk.classify.apply_features(extract_features, test_list)
    model = str(input("Please give the model you want to use to train (nb or svm) : "))

    start = time.clock()
    classifier = None
    if model == 'nb':
        print('Train on %d instances, Test on %d instances using Naive Bayes Classifier...' % (len(training_set), len(test_set)))
        classifier = nltk.NaiveBayesClassifier.train(training_set) # time consuming operation
    elif model == 'svm':
        print('Train on %d instances, Test on %d instances using Support Vector Machine...' % (len(training_set), len(test_set)))
        classifier = nltk.classify.SklearnClassifier(LinearSVC()).train(training_set)
    
    print('Training complete.')
    print("Training time:", str((time.clock() - start)),"secs")
    start = time.clock()
    accuracy = nltk.classify.util.accuracy(classifier, test_set) # time consuming operation
    print("Get accuracy time:", str((time.clock() - start)),"secs")
    print('accuracy:', accuracy)
    if model == 'nb':
        classifier.show_most_informative_features(20)
    return classifier
