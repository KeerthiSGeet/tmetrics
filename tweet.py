# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing
import re

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

from Credentials import *    # This will allow us to use the keys as variables

# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

extractor = twitter_setup()

# We create a tweet list as follows:
topic=input("Enter a topic ")
print(topic)

tweets = extractor.user_timeline(screen_name=topic, count=200)

print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent 5 tweets:
print("5 recent tweets:\n")
f = open("demofile.txt", "a")
for tweet in tweets: #tweets[:5]
   twit = re.sub(r'http\S+',"", tweet.text)
   twit = re.sub(r'@[\r\n]*$',"", twit)

   f.write(twit+'\n')

   

f.close()

