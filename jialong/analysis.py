#! /usr/local/bin/python3

import training

f = open('datafile','w')
for num in range(100, 501, 100):
    classifier, training_time, accuracy = training.do_training(num, 'nb')
    f.write(str(num) + '   ' + str(training_time) + '   ' + str(accuracy) + '\n')
f.close()