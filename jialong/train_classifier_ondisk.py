#! /usr/local/bin/python3

import pickle
from classifier import MyClassifier

# train the data
number = str(input("Please give how many data you want to train: "))
model = str(input("Please give the model you want to use to train (nb or svm) : "))
classifier = MyClassifier(number, model)
classifier.train()

# save classifier on the disk
f = open('../model/classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()