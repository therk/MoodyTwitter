#!/usr/bin/env python
import signal
import sys

import SimpleOauth

queryStr = urllib.quote(' '.join(sys.argv[1:]))

# does a cleanup when ctr-c is used to exit during the stream
def signal_handler(signal, frame):
    sys.exit(2)

signal.signal(signal.SIGINT, signal_handler)

response = SimpleOauth.getUrlResponse("https://stream.twitter.com/1.1/statuses/sample.json")
for line in response:
  print line.strip()
