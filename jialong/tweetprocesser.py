
import re
import nltk.classify

emoticons = [':)',':-)',':D','=D','=)',':(',':-(','=(','=[',')-:']
slang = {'lol':'happy', 'lmao':'happy','rof':'happy','jk':'joking','wanna':'want to',
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
        if part in emoticons: continue
        if part.lower() in slang:
            res.append(slang[part.lower()])
        if part.lower() in stopwords: continue
        if len(part) < 3 and part.lower() != 'no': continue
        res.append(part)
    return res

def clean_symbol(tweet):
    t = re.sub(r'@[a-zA-Z0-9_]+\s+|#[a-zA-Z0-9]+\s+|http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', '', tweet)
    t = preprocess(nltk.word_tokenize(t), get_stop_words())
    return t

def get_stop_words():
    stopwords = []
    f = open('../dataset/stop-words_english.txt','r')
    for word in f:
        stopwords.append(word.rstrip())
    f.close()
    return stopwords