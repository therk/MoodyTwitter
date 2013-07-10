#!/usr/local/bin/python

import sys
import json

def sentiment(scores, text):
    words = text.split();
    total_score = 0;
    for word in words:
        #print word
        if scores.has_key(word) == 1:
            #print scores[word]
            total_score = total_score + scores[word]

    print total_score

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = json.loads(line)
        tweet_text = tweet['text']
        sentiment(scores, tweet_text)


if __name__ == '__main__':
    main()
