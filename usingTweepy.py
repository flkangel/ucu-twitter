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
#Search 10 tweets using a keyword in spanish
query = "RaulSendic_uy"
language = "es"
count_tweets = 100
contador = 0
with open("RaulSendic_uy.txt", "w") as text_file:
    for tweet in tweepy.Cursor(api.search,
                               q= query,
                               count=count_tweets,
                               lang= language).items():
        print ("\n\t@"+ tweet.user.screen_name," Tweetió:"+ "\n\t" + tweet.text, file = text_file)
        contador = contador + 1
print (str(contador))
# Calling the function
#resTweets = api.search(q = query, rpp = count, lang = language,)
#printing results
#text_list = []
#for tweet in resTweets:
 #   print ("\n\t@"+ tweet.user.screen_name," Tweetió:"+ "\n\t" + tweet.text) #Debugging
    #text_list.append(tweet.user.screen_name + tweet.text)
#print (text_list)
#Query a Monkeylearn
#for comment in text_list: 
 #   resML = ML.classifiers.classify(MODULE_ID, text_list, sandbox=False)
#for items in text_list.index,resML.result:
 #   print(items)