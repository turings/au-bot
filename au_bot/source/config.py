import tweepy
import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger()

def create_api():
    load_dotenv("files/variables.env")
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("API creation error", exec_info=True)
        raise e
    logger.info("API created")
    return api
