import sys
import requests
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
url = 'https://api.twitter.com/1.1/'
endpoint = 'statuses/user_timeline.json'
screen_name ='MasterChef_UY'
count = '2'
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
response = requests.get(url+endpoint+'?screen_name='+screen_name+'&count='+count, auth=auth)
response2= requests.get("https://twitter.com/search?q=%40tangelbustamante", auth=auth)
if response.status_code == 200:
    print ("Authorization Successful")
if response2.status_code == 200:
    print ("Lectura de Angel bien")
print(response2)
for tweet in response2.json():
    text_list.append(json.dumps(tweet['text']))
print(text_list)
#Query a Monkeylearn
#for comment in text_list: 
 #   res = ML.classifiers.classify(MODULE_ID, text_list, sandbox=False)
#print (res.result)