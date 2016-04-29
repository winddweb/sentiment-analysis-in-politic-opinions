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

class MyClassifier():

    def __getstate__(self): return self.__dict__
    def __setstate__(self, d): self.__dict__.update(d)

    def __init__(self, number, model):
        self.word_features = []
        self.classifier = None
        self.model = model
        self.number = number
        self.accuracy = 0
        self.training_time = 0

    def get_words_in_tweets(self, tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words

    def get_word_features(self, wordlist):
        wordlist = nltk.FreqDist(wordlist)
        return wordlist.keys()

    def extract_features(self, document):
        document_words = set(document)
        features = {}
        for word in self.word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features

    def train(self):
        trainingRow = int(self.number) / 2
        firstNegRow = 0
        firstPosRow = 800000
        # total positive tweets training set : 248,576
        enc = 'iso-8859-15'
        pos_tweets = []
        neg_tweets = []
        rowNum = 0
        print('Processing tweets ...')
        # read csv training set
        csvf = open('../data/training.csv', 'r', encoding=enc)
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
                else: break
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
   
        self.word_features = self.get_word_features(self.get_words_in_tweets(tweets))
        training_set = nltk.classify.apply_features(self.extract_features, training_list)
        test_set = nltk.classify.apply_features(self.extract_features, test_list)

        start = time.clock()
        if self.model == 'nb':
            print('Train on %d data, Validate on %d data using Naive Bayes Classifier...' % (len(training_set), len(test_set)))
            self.classifier = nltk.NaiveBayesClassifier.train(training_set) # time consuming operation
        elif self.model == 'svm':
            print('Train on %d data, Validate on %d data using Support Vector Machine...' % (len(training_set), len(test_set)))
            self.classifier = nltk.classify.SklearnClassifier(LinearSVC()).train(training_set)
    
        print('Training complete.')
        self.training_time = str((time.clock() - start))
        print("Training time:", self.training_time,"secs")
        self.accuracy = nltk.classify.util.accuracy(self.classifier, test_set) # time consuming operation
        print('Validation Accuracy is :', self.accuracy)
        if self.model == 'nb':
            self.classifier.show_most_informative_features(15)
