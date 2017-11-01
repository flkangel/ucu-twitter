import sys
import requests
import json
import twitter
from time import sleep
from monkeylearn import MonkeyLearn
from requests_oauthlib import OAuth1
#Monkerlearn Developer APP Credentials
ML = MonkeyLearn('c07510c44c6c852ec2e9809fe306ae931457f0d1')
MODULE_ID = 'cl_u9PRHNzf'
# Twitter Developer APP Credentials
api = twitter.Api(consumer_key='xMtOqSQCcT5Unc0JEKmlmTsU6',
                  consumer_secret = 'jbKHeCK6Z1nEHva4tMPkjZLddI1znmahBjDDE2cNGevilZV2v5',
                  access_token_key = '80344712-W2bIaCbzKcZAEdNHBTgB6iA8ScO1gX6LwOF6u6npB',
                  access_token_secret = 'RrYXlNI2t8PihhrF3SwYzj2hX5IWfoF8kZFpIjd64cjJP')
screen_name ='MasterChef_UY'
print(api.VerifyCredentials())


#Query a Monkeylearn
#for comment in text_list: 
 #   res = ML.classifiers.classify(MODULE_ID, text_list, sandbox=False)
#print (res.result)