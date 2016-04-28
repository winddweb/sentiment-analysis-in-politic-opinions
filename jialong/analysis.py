#! /usr/local/bin/python3

import sys
import training

# ./analysis.py <start> <end> <step> <model>: ./analysis.py 100 5001 300 nb
start = int(sys.argv[1])
end = int(sys.argv[2])
step = int(sys.argv[3])
model = sys.argv[4]

f = open('datafile','w')
for num in range(start, end, step):
    classifier, training_time, accuracy = training.do_training(num, model)
    f.write(str(num) + '   ' + str(training_time) + '   ' + str(accuracy) + '\n')
f.close()