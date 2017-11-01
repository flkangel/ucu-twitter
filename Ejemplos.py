#Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.home_timeline()

#Para ver mi Timeline
# foreach through all tweets pulled
#for tweet in public_tweets:
   # printing the text stored inside the tweet object
 #  print (tweet.text)


#Para ver Timeline de otro usuario
# The Twitter user who we want to get tweets from
name = "nytimes"
# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.text)
