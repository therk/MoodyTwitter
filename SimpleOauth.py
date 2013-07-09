import oauth2 as oauth
import urllib2 as urllib
import sys
import ConfigParser
import os

def getUrlResponse(url):
	configFile = 'oauth.cfg'
	if not os.path.isfile(configFile):
		print "Must have " + configFile + " file. You can create it based on sample_oauth.cfg file."
		sys.exit(1)

	config = ConfigParser.RawConfigParser()
	config.read(configFile)

	oauthToken = oauth.Token(key=config.get('Token', 'key'), 
							secret=config.get('Token', 'secret'))
	oauthConsumer = oauth.Consumer(key=config.get('Consumer', 'key'), 
							secret=config.get('Consumer', 'secret'))

	request = oauth.Request.from_consumer_and_token(oauthConsumer,
	                                             token=oauthToken,
	                                             http_method="GET",
	                                             http_url=url,
	                                             parameters=[])

	request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), oauthConsumer, oauthToken)

	opener = urllib.OpenerDirector()
	opener.add_handler(urllib.HTTPHandler())
	opener.add_handler(urllib.HTTPSHandler())

	response = opener.open(request.to_url())

	return response