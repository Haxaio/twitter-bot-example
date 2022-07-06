import tweepy
import os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", os.getenv("TWITTER_CONSUMER_KEY"))
auth.set_access_token("ACCESS_TOKEN", os.getenv("TWITTER_ACCESS_TOKEN"))

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
