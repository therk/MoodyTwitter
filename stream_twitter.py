#!/usr/bin/env python
import signal
import sys
import time
import exceptions

import SimpleOauth
# get timeout in seconds from command line or default to 60 seconds
try:
	timeoutTime = float(len(sys.argv)>1 and sys.argv[1] or 60) + time.time()
except exceptions.ValueError:
	print "Must supply numeric value for seconds"
	exit(1)

# does a cleanup when ctr-c is used to exit during the stream
def signal_handler(signal, frame):
    sys.exit(2)
signal.signal(signal.SIGINT, signal_handler)

response = SimpleOauth.getUrlResponse("https://stream.twitter.com/1.1/statuses/sample.json")
for line in response:
  print line.strip()
  if timeoutTime <= time.time():
  	sys.exit()

