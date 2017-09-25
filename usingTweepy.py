import sys
import requests
import tweepy
import json
from time import sleep
from monkeylearn import MonkeyLearn
from requests_oauthlib import OAuth1
#Monkerlearn Developer APP Credentials
ML = MonkeyLearn('44c6c8526ae93145ec2e9809fe307f0d1c07510c')
MODULE_ID = 'cl_u9PRHNzf'
# Twitter Developer APP Credentials
API_KEY = 'SQCcTEKmlnxMtOqc0J'
API_SECRET = 'jbKHeCK6Z1nEHva4tMPkjjLddI1znmahBv5'
ACCESS_TOKEN = 'ZAEdNHBTgB6iA8ScO10mTsU65U344712-W2bIaCbzKcgfoF8kZFpIjd6X6LwOF6u6npB'
ACCESS_TOKEN_SECRET = 'RrYSwYzj2hX5IW4cXlNI2tDDE2cNGevilZV2Z8PihhrF3jJP'
#Setting up authentication Objects
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token( ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Authentication
api = tweepy.API(auth)
#Search 10 tweets using a keyword in spanish
query = "MasterChefUY"
language = "es"
count = 1
# Calling the funciton
resTweets = api.search( q = query, lang = language, rpp = count )
#printing results
text_list = []
for tweet in resTweets:
    #print (tweet.user.screen_name,"tweetio: ",tweet.text) //Debugging
    text_list.append(tweet.user.screen_name + tweet.text)
#Query a Monkeylearn
for comment in text_list: 
    resML = ML.classifiers.classify(MODULE_ID, text_list, sandbox=False)
for items in text_list.index,res.result:
    print(items)
