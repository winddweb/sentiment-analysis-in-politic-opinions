#! /usr/local/bin/python3

import sys
import training

# ./analysis.py <start> <end> <step> <model> <mode>:
# eg ./analysis.py 100 5001 300 nb a
start = int(sys.argv[1])
end = int(sys.argv[2])
step = int(sys.argv[3])
model = sys.argv[4]
mode = sys.argv[5] # 'w', 'a'

f = open(model + 'data', mode) # model name as file name
for num in range(start, end, step):
    classifier, training_time, accuracy = training.do_training(num, model)
    f.write(str(0.8*num) + '   ' + str(training_time) + '   ' + str(accuracy) + '\n')
f.close()