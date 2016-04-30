#! /usr/local/bin/python3

import sys
import random
import csv
import tweetprocesser
import nltk.classify
from classifier import MyClassifier

# ./testdata_accuracy_analysis.py <start> <end> <step> <model> <mode>:
# ./testdata_accuracy_analysis.py 125 12501 625 nb a
# ./testdata_accuracy_analysis.py 125 25001 1250 nb a
start = int(sys.argv[1])
end = int(sys.argv[2])
step = int(sys.argv[3])
model = sys.argv[4]
mode = sys.argv[5] # 'w', 'a'

tweets = tweetprocesser.label_test_tweets()

f = open(model + 'test', mode) # model name as file name
for num in range(start, end, step):
    classifier = MyClassifier(num, model)
    classifier.train()
    test_set = nltk.classify.apply_features(classifier.extract_features, tweets)
    test_accuracy = nltk.classify.util.accuracy(getattr(classifier, 'classifier'), test_set)
    # Number | Accuracy
    f.write(str(0.8*num) + '   ' + str(test_accuracy) + '\n')
f.close()