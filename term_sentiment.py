#!/usr/local/bin/python

import sys
import json

def newSentiment(scores, text):
    newTerms = {}
    words = text.split();
    score = 0;
    wordCount = 0;

    for word in words:
        if scores.has_key(word):
            score = scores[word] + score
            wordCount = wordCount + 1
        else:
            newTerms[word] = 0

    if wordCount > 0:
        for term in newTerms:
            newTerms[term] = score / wordCount

    return newTerms

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    newTerms = {}

    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

    tweetFile = open(sys.argv[2])
    for line in tweetFile:
        tweet = json.loads(line)

        if tweet.has_key('text'):
            tweetText = tweet['text']
            newTweetTerms = newSentiment(scores, tweetText)
            for term in newTweetTerms:
                if newTerms.has_key(term):
                    newTerms[term].append(newTweetTerms[term])
                else:
                    newTerms[term] = [newTweetTerms[term]]

    for term in newTerms:
        meanScore = sum(newTerms[term]) / float(len(newTerms[term]))
        print term + ' ' + str(meanScore)

if __name__ == '__main__':
    main()
