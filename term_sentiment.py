#!/usr/bin/env python

import sys
import json
from optparse import OptionParser

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

    parser = OptionParser()
    parser.add_option("-s", "--sentiment", dest="sentimentFilePath",
                  help="tab delimited file with word and sentiment value. Example: 'acrimonious  -3'", 
                  metavar="FILE",
                  default="AFINN-111.txt")
    parser.add_option("-t", "--tweet", dest="tweetFilePath",
                  help="Tweet output in JSON format with one line per tweet", 
                  metavar="FILE",
                  )

    (options, args) = parser.parse_args()
    if not options.tweetFilePath:
        parser.error("Must supply tweet file")

    try:
        sentimentFile = open(options.sentimentFilePath)
    except IOError:
        print "Unable to open sentiment file: " + options.sentimentFilePath
        exit(1)

    scores = {}
    newTerms = {}

    for line in sentimentFile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    try:
        tweetFile = open(options.tweetFilePath)
    except IOError:
        print "Unable to open tweet file: " + options.tweetFilePath
        exit(1)

    for line in tweetFile:
        tweet = json.loads(line)

        if tweet.has_key('text') and tweet.has_key('lang') and tweet['lang'] == 'en':
            tweetText = tweet['text']
            newTweetTerms = newSentiment(scores, tweetText)
            for term in newTweetTerms:
                # skip words less then 2 chars
                if len(term):
                    next
                if newTerms.has_key(term):
                    newTerms[term].append(newTweetTerms[term])
                else:
                    newTerms[term] = [newTweetTerms[term]]

    for term in newTerms:
        meanScore = sum(newTerms[term]) / float(len(newTerms[term]))
        print term + "\t" + str(meanScore)

if __name__ == '__main__':
    main()
