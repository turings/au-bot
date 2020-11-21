import tweepy
import logging
import os
from source.variables import consumer_key
from source.variables import consumer_secret
from source.variables import access_token
from source.variables import access_token_secret

logger = logging.getLogger()

def create_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("API creation error;;", exec_info=True)
        raise e
    logger.info("API created~")
    return api
