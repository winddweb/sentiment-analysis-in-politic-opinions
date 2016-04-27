#! /usr/bin/python3

import csv
import sys
import re
from nltk.tokenize import word_tokenize

def replace_tweet_tokens(tweet_text):
    emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""

    regex_str = [
        #emoticons_str,
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r'(?:\S)' # anything else
    ]

    tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
    emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

    def shorten_word(word):
        b = (None,None)
        new_word = []

        for char in word:
            if not b[0]:
                new_word.append(char)
            elif (b[1], char) != b:
                new_word.append(char)

            b = (b[1], char)

        return ''.join(new_word)

    def tokenize(s):
        return tokens_re.findall(s)

    def preprocess(s, lowercase=False):
        tokens = tokenize(s)
        if lowercase:
            tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]

        filtered_tokens = [x for x in tokens if len(x) > 2 and x.lower() is not 'no' and '@' not in x and '#' not in x and r'http://' not in x]


        filtered_tokens = list(map(shorten_word, filtered_tokens)) # shorten duplicate characters e.g. coooooll to cooll

        """
        def filter_tokens(s):
            if len(s) > 2 and '@' not in s and '#' not in s:
                return s
            elif s in ['no']:
                return s

        filtered_tokens = list(map(filter_tokens, tokens))
        """

        # filter not None
        # [x for x in L if x is not None]

        # stop words
        f_stop_words = open('../resource/stop-words_english.txt', 'r')
        stop_words = list(map(lambda x: x.strip('\n') , f_stop_words.readlines()))
        exclude_append = ["it's", "i'm", "that's", "how's"]
        stop_words.extend(exclude_append)

        filtered_tokens = [x for x in filtered_tokens if x not in stop_words]

        return filtered_tokens

    return preprocess(tweet_text, True)

def process_tweet(tweet_obj):
    """
    0 - the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
    1 - the id of the tweet (2087)
    2 - the date of the tweet (Sat May 16 23:58:44 UTC 2009)
    3 - the query (lyx). If there is no query, then this value is NO_QUERY.
    4 - the user that tweeted (robotickilldozr)
    5 - the text of the tweet (Lyx is cool)
    """
    polarity, tweet_id, date, query, username, tweet = tweet_obj

    # output
    print(replace_tweet_tokens(tweet))

    # print(word_tokenize(tweet))


if __name__ == '__main__':

    with open('../data/test-data-5.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            process_tweet(row)
