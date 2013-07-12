MoodyTwitter
============

###	Code for CNJ DIG Meetup on Analyze Moody Twitter
Examples in this project are based on the Twitter assignment in Coursera "Introduction to Data Science" MOOC (https://www.coursera.org/course/datasci)

Files
-----
*	1k_tweets.txt
*	AFINN-111.txt
*	AFINN-README.txt
*	oauth.cfg
*	sample_oauth.cfg
*	search_twitter.py
*	stream_twetter.py
*	term_sentiment.py
*	tweet_sentiment.py
*	happiest_state.py
*	SimpleOauth.py

Configuration & Installation
----------------------------
### Pythong Install
1.	On Windows use Python 2.7.5 Windows Installer - http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi
2.	Install easy_install.exe by running https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe#md5=57e1e64f6b7c7f1d2eddfc9746bbaf20
3.	Install Oauth by running "easy_install.exe oauth2"

### Twitter Dev Account
1.	Register on http://dev.twitter.com
2.	Create Twitter Application
3.	Create Access Token for your Twitter Application
4.	Copy sample_oauth.cfg to oauth.cfg and copy Consumer key, Consumer secret, Access token, and Access token Secret values from your Twitter Application to oauth.cfg


Twitter API
-----------
*	API v1.1 is the current version. It only supports JSON and requires Oauth 1.0a. 
*	API v1.0 has been retired on June 11, 2013. It was a simpler API in that it didn't require authentication.

Resources on Twitter Sentiment Analysis
---------------------------------------
*	"From Tweets to Polls: Linking Text Sentiment to Public Opinion Time Series" - http://www.cs.cmu.edu/~rbalasub/publications/oconnor_balasubramanyan_routledge_smith.icwsm2010.tweets_to_polls.pdf
*	"Twitter mood predicts the stock market" - http://www.relevantdata.com/pdfs/IUStudy.pdf
*	http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

Resources on Statistics and Natural Language
--------------------------------------------
*	Free and Open Textbook on Statistics - http://www.openintro.org/stat/
*	Course on Natrual Language Processing - https://www.coursera.org/course/nlp 

Resources on Python
-------------------
*	Google's Python Class - https://developers.google.com/edu/python
*	Code Academy Python - http://www.codecademy.com/tracks/python
