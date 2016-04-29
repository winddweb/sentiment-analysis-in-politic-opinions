#! /usr/local/bin/python3

import pickle
from classifier import MyClassifier

# train 25000 data
model = str(input("Please give the model you want to use to train (nb or svm) : "))
classifier = MyClassifier('25000', model)
classifier.train()

f = ''
# save classifier on the disk
if model == 'nb':
	f = open('../model/nb_classifier.pickle', 'wb')
elif model == 'svm':
	f = open('../model/svm_classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()