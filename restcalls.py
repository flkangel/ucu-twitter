import sys
import requests
import json
from requests_oauthlib import OAuth1
# Twitter Developer APP Credentials
API_KEY = 'xMtOqSQCcT5Unc0JEKmlmTsU6'
API_SECRET = 'jbKHeCK6Z1nEHva4tMPkjZLddI1znmahBjDDE2cNGevilZV2v5'
ACCESS_TOKEN = '80344712-W2bIaCbzKcZAEdNHBTgB6iA8ScO1gX6LwOF6u6npB'
ACCESS_TOKEN_SECRET = 'RrYXlNI2t8PihhrF3SwYzj2hX5IWfoF8kZFpIjd64cjJP'
url = 'https://api.twitter.com/1.1/'
endpoint = 'statuses/user_timeline.json'
screen_name ='MasterChef_UY'
count = '3'
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
response = requests.get(url+endpoint+'?screen_name='+screen_name+'&count='+count, auth=auth)
if response.status_code == 200:
    print ("Authorization Successful")
for tweet in response.json():
  print (json.dumps(tweet['text']))