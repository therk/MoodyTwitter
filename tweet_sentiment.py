#!/usr/bin/env python
import sys
import json

def sentiment(scores, text):
    words = text.split();
    totalScore = 0;
    for word in words:
        if scores.has_key(word) == 1:
            totalScore = totalScore + scores[word]
    print text + "\t" + str(totalScore)

def main():
    sentimentFile = open(sys.argv[1])
    scores = {}
    for line in sentimentFile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = json.loads(line)
        if tweet.has_key('text'):
            tweetText = tweet['text']
            sentiment(scores, tweetText)

if __name__ == '__main__':
    main()
