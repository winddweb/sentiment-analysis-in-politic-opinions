#! /usr/local/bin/python3

import sys
from classifier import MyClassifier

# ./validation_data_analysis.py <start> <end> <step> <model> <mode>:
# ./validation_data_analysis.py 125 12501 625 nb a
start = int(sys.argv[1])
end = int(sys.argv[2])
step = int(sys.argv[3])
model = sys.argv[4]
mode = sys.argv[5] # 'w', 'a'

f = open(model + 'validation', mode) # model name as file name
for num in range(start, end, step):
    classifier = MyClassifier(num, model)
    classifier.train()
    training_time = getattr(classifier, 'training_time')
    accuracy = getattr(classifier, 'accuracy')
    # Number | Training time | Accuracy
    f.write(str(0.8*num) + '   ' + str(training_time) + '   ' + str(accuracy) + '\n') 
f.close()