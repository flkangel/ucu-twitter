import sys
import requests
import tweepy
import json
from time import sleep
from monkeylearn import MonkeyLearn
from requests_oauthlib import OAuth1
#Monkerlearn Developer APP Credentials
ML = MonkeyLearn('cae9314570751080c2e9f0d19fe306c44c6c852e')
MODULE_ID = 'cl_u9PRHNzf'
# Twitter Developer APP Credentials
API_KEY = 'OqSQnc0JEKmlxMtmCcT5UTsU6'
API_SECRET = 'jbKHeCK6Z1nEHva4tMPkjZLddI12cNGevilZV2vznmahBjDDE5'
ACCESS_TOKEN = '34471280-W2biA8ScO1gX6LwOpBF6u6n'
ACCESS_TOKEN_SECRET = 'ihhrFkZFpIjd64RrYXlNI2t8Pcj3SfoF8wYzj2hX5IWJP'
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
