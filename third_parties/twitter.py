import os
from datetime import datetime, timezone
import logging

import tweepy


def scrape_user_tweets(username, num_tweets):
    """
    Scrapes the last num_tweets tweets from a user's timeline.
    Does not include retweets or replies.
    Returns the tweets as a list of dicts with the fields:
        - created_at
        - text
        - URL
    """

    tweepy_client = tweepy.Client(
        consumer_key=os.environ["TWITTER_API_KEY"],
        consumer_secret=os.environ["TWITTER_API_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
        bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    )

    user_info = tweepy_client.get_me()
    print(user_info)
    return user_info
