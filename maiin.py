import sys
import requests 
import json
# Twitter module for Python3
import tweepy 
# Disable warnings
requests.packages.urllib3.disable_warnings() 
from tweepy import OAuthHandler
# Twitter Developer APP Credentials
consumer_key = 'xMtOqSQCcT5Unc0JEKmlmTsU6'
consumer_secrect = 'jbKHeCK6Z1nEHva4tMPkjZLddI1znmahBjDDE2cNGevilZV2v5'
access_token = '80344712-W2bIaCbzKcZAEdNHBTgB6iA8ScO1gX6LwOF6u6npB'
access_secret = 'RrYXlNI2t8PihhrF3SwYzj2hX5IWfoF8kZFpIjd64cjJP'
#Authentication
auth = OAuthHandler(consumer_key,consumer_secrect)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)
#Test1: Reading my onw feed
def process_or_store(tweet):
    print(json.dumps(tweet))
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
#Test2: List of my followers
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)