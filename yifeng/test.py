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
        emoticons_str,
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:\S)' # anything else
    ]

    tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
    emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

    def tokenize(s):
        return tokens_re.findall(s)

    def preprocess(s, lowercase=False):
        tokens = tokenize(s)
        if lowercase:
            tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens

    return preprocess(tweet_text)



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



    print(replace_tweet_tokens(tweet))

if __name__ == '__main__':

    with open('../data/test-data-5.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            process_tweet(row)


