import sys
import requests
import tweepy
import json
from time import sleep
from monkeylearn import MonkeyLearn
from requests_oauthlib import OAuth1
#Monkerlearn Developer APP Credentials
ML = MonkeyLearn('c07510c44c6c852ec2e9809fe306ae931457f0d1')
MODULE_ID = 'cl_u9PRHNzf'
# Twitter Developer APP Credentials
API_KEY = 'xMtOqSQCcT5Unc0JEKmlmTsU6'
API_SECRET = 'jbKHeCK6Z1nEHva4tMPkjZLddI1znmahBjDDE2cNGevilZV2v5'
ACCESS_TOKEN = '80344712-W2bIaCbzKcZAEdNHBTgB6iA8ScO1gX6LwOF6u6npB'
ACCESS_TOKEN_SECRET = 'RrYXlNI2t8PihhrF3SwYzj2hX5IWfoF8kZFpIjd64cjJP'
#Setting up authentication Objects
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token( ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Authentication
api = tweepy.API(auth)
#Search tweets using a keyword in spanish
query = "MasterChefUY"
language = "es"
# Calling the funciton
results = api.search( q = query, lang = language)
#printing results
for tweet in results:
    print (tweet.user.screen_name,"tweetio: ",tweet.text)
