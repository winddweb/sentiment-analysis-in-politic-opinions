#! /usr/local/bin/python3

import csv
import nltk
import re
import time
import nltk.classify
from random import shuffle
from nltk.classify import apply_features
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

# clean up tweets:
# remove emoticons
# remove links(http://,https://)
# remove #, @
# remove stop words
# remove any character which len() < 3 
def preprocess(tweets, stopwords):
    res = []
    for part in tweets:
        if part in emoticons: continue
        if part.lower() in slang:
            res.append(slang[part.lower()])
        if part.lower() in stopwords: continue
        if len(part) < 3 and part.lower() != 'no': continue
        res.append(part)
    return res

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


emoticons = [':)',':-)',':D','=D','=)',':(',':-(','=(','=[',')-:']
special_symbol = ['#', '@']
url = ['http://', 'https://']
slang = {'lol':'happy', 'lmao':'happy','rof':'happy','jk':'joking','wanna':'want to',
        'dam':'annoying', 'hagn':'good', 'hand':'nice', 'stfu':'annoying', 
        'tyia':'thankful', 'tyvm':'thankful','yw':'welcome'
}

# maxRow should get user input
userinput = str(input("Please give how many data you want to train: "))
trainingRow = int(userinput) / 2
firstNegRow = 0
firstPosRow = 800000
# total positive tweets training set : 248,576
rowNum = 0
enc = 'iso-8859-15'
stopwords = []
pos_tweets = []
neg_tweets = []

f = open('stop-words_english.txt','r')
for word in f:
    stopwords.append(word.rstrip())
f.close()

print('Processing tweets ...')
# read csv training set
csvf = open('training.csv', 'r', encoding=enc)
reader = csv.reader(csvf)
for row in reader:   # iterates the rows of the file in orders
    if rowNum < firstNegRow + trainingRow:
        tweet = re.sub(r'@[a-zA-Z0-9_]+\s+|#[a-zA-Z0-9]+\s+|http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', '', row[-1])
        tweet = preprocess(nltk.word_tokenize(tweet), stopwords)
        neg_tweets.append((tweet, 'neg'))
        rowNum += 1
    else:
        if rowNum < firstPosRow: rowNum += 1
        elif rowNum < firstPosRow + trainingRow:
            tweet = re.sub(r'@[a-zA-Z0-9_]+\s+|#[a-zA-Z0-9]+\s+|http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', '', row[-1])
            tweet = preprocess(nltk.word_tokenize(tweet), stopwords)
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

word_features = get_word_features(get_words_in_tweets(tweets))
training_set = nltk.classify.apply_features(extract_features, training_list)
test_set = nltk.classify.apply_features(extract_features, test_list)
model = str(input("Please give the model you want to use to train (nb or svm) : "))
#print('Train on %d instances, Test on %d instances ...' % (len(training_set), len(test_set)))
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
elif model == 'svm':
    #print(classification_report(training_set, test_set, target_names=['pos','neg']))
    pass

# simple test
tweet = 'Your song is annoying' # Negative
print('The test result is ' + classifier.classify(extract_features(tweet.split())))

