#!/usr/bin/env python
import signal
import sys
import json
import urllib2 as urllib

import SimpleOauth

# Make sure that we get a search string as an arument
if len(sys.argv) == 1:
	print "Please provide twitter search string as argument"
	sys.exit(1)

# First element of argv is the command itself, so we skip it using [1:] slice 
# Also, URL encode the command line input so it can be used in the REST url
queryStr = urllib.quote(' '.join(sys.argv[1:]))

response = SimpleOauth.getUrlResponse("https://api.twitter.com/1.1/search/tweets.json?src=typd&lang=en&q=" + queryStr)
tweets = json.load(response)

if not tweets.has_key('statuses'):
	print "No Results"
	sys.exit(0)

results = tweets['statuses']

for tweet in results:
    print tweet["text"]
