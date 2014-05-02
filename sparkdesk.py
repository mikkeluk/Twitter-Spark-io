

#pplication settings
#Your application's API keys are used to authenticate requests to the Twitter Platform.
#Access level	 Read-only (modify app permissions)
#API key	 h9AHWnO4kUEff8QSOCgS24dmT (manage API keys)
#Callback URL	None
#Sign in with Twitter	No
#App-only authentication	https://api.twitter.com/oauth2/token
#Request token URL	https://api.twitter.com/oauth/request_token
#Authorize URL	https://api.twitter.com/oauth/authorize
#Access token URL	https://api.twitter.com/oauth/access_token


#API key	h9AHWnO4kUEff8QSOCgS24dmT
#API secret	gAnYLUS1kO9EKeFsdPJMfwPwLtck5LMH1ZGl5dhPZmgmHLRz97
#Access level	 Read-only (modify app permissions)
#Owner	Coinbench
#Owner ID	2394495780


import tweepy
import sys

consumer_key = "h9AHWnO4kUEff8QSOCgS24dmT"
consumer_secret = "gAnYLUS1kO9EKeFsdPJMfwPwLtck5LMH1ZGl5dhPZmgmHLRz97"

access_token= "2394495780-1zfGMAq7GYMr62ndGpLCa8o459DQK8sJ3Gr6Mma"
access_token_secret = "J89Wb4aV9nZVh6LAGl9lKFczKgm69QglyqJN9wfRkIedg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    strs = tweet.text
    sys.stdout.encoding
    print strs



#auth = tweepy.OAuthHandler("2394495780-1zfGMAq7GYMr62ndGpLCa8o459DQK8sJ3Gr6Mma", "J89Wb4aV9nZVh6LAGl9lKFczKgm69QglyqJN9wfRkIedg")