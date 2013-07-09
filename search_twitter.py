#!/usr/bin/env python

import oauth2 as oauth
import urllib2 as urllib
import signal
import sys
import json
import ConfigParser
import os

configFile = 'oauth.cfg'
if not os.path.isfile(configFile):
	print "Must have " + configFile + " file. You can create it based on sample_oauth.cfg file."
	sys.exit(1)

config = ConfigParser.RawConfigParser()
config.read(configFile)

print config.get('Token', 'key')

if len(sys.argv) == 1:
	print "Please provide twitter search string as argument"
	sys.exit(1)

queryStr = urllib.quote(' '.join(sys.argv[1:]))

# does a cleanup when ctr-c is used to exit during feed
def signal_handler(signal, frame):
    sys.exit(2)
signal.signal(signal.SIGINT, signal_handler)

oauthToken = oauth.Token(key=config.get('Token', 'key'), 
						secret=config.get('Token', 'secret'))
oauthConsumer = oauth.Consumer(key=config.get('Consumer', 'key'), 
						secret=config.get('Consumer', 'secret'))

request = oauth.Request.from_consumer_and_token(oauthConsumer,
                                             token=oauthToken,
                                             http_method="GET",
                                             http_url="https://api.twitter.com/1.1/search/tweets.json?src=typd&lang=en&q=" + queryStr, 
                                             parameters=[])

request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), oauthConsumer, oauthToken)

opener = urllib.OpenerDirector()
opener.add_handler(urllib.HTTPHandler())
opener.add_handler(urllib.HTTPSHandler())

response = opener.open(request.to_url())

def signal_handler(signal, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

tweets = json.load(response)

print tweets.keys()

if not tweets.has_key('statuses'):
	print "No Results"
	sys.exit(0)

results = tweets['statuses']

for tweet in results:
    print tweet["text"]
