f = open('../resource/stop-words_english.txt', 'r')
x = list(map(lambda x: x.strip('\n') , f.readlines()))

print(x)