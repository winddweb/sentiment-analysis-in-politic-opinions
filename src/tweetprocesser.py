import re
import csv
import random
import nltk.classify

emoticons = [':)',':-)',':D','=D','=)',':(',':-(','=(','=[',')-:']
slang = {'lol':'laugh', 'lmao':'laugh','rof':'happy','jk':'joking','wanna':'want to',
        'dam':'annoying', 'hagn':'good', 'hand':'nice', 'stfu':'annoying', 
        'tyia':'thankful', 'tyvm':'thankful','yw':'welcome'
}

# clean up tweets:
# remove emoticons
# remove links(http://,https://)
# remove #, @
# remove stop words
# remove any character which len() < 3 
def preprocess(tweets, stopwords):
    res = []
    for part in tweets:
        part = part.lower()
        if part in emoticons: continue
        if part in slang:
            res.append(slang[part])
            continue
        if part in stopwords: continue
        if len(part) < 3 and part != 'no': continue
        if part == '...': continue
        if part == "n't": 
            res.append('not')
            continue
        res.append(part)
    return res

def clean_symbol(tweet):
    t = re.sub(r'@[a-zA-Z0-9_]+\s+|#[a-zA-Z0-9]+\s+|http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', '', tweet)
    t = preprocess(nltk.word_tokenize(t), get_stop_words())
    return t

def get_stop_words():
    stopwords = []
    f = open('../resource/stop-words_english.txt','r')
    for word in f:
        stopwords.append(word.rstrip())
    f.close()
    return stopwords

def label_test_tweets():
    enc = 'iso-8859-15'
    tweets = []
    print('Tagging test data...')
    # read all the test data
    csvf = open('../data/test.csv', 'r', encoding=enc)
    reader = csv.reader(csvf)
    for row in reader:   # iterates the rows of the file in orders
        tweet = clean_symbol(row[-1])
        if row[0] == '0': tweets.append((tweet, 'neg'))
        elif row[0] == '4': tweets.append((tweet, 'pos'))
    csvf.close()
    random.shuffle(tweets)
    return tweets
