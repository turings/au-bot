import tweepy
import logging
import time
import string
import os
from source.config import create_api
from source.tools import create_file
from source.role import get_role
from source.character import get_xover_character
from source.fandom import get_xover_fandom
from source.setting import get_setting

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, since_id):
    logger.info("Loading")
    # Load file containing read tweets (create if doesn't exist)
    create_file(os.environ['TWEETS_FILE'])
    f = open(os.environ['TWEETS_FILE'], "r").readlines()
    # Retrieve mentions
    logger.info("Getting mentions")
    new_since_id = since_id
    # Look at timeline; loop through tweets after last mention
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        # Get new last mention ID
        new_since_id = max(tweet.id, new_since_id)
        # If this tweet already exists in the file, ignore it
        # if str(tweet.id) + "\n" in f:
            # continue
        logger.info("Recording tweet ID")
        # Add this tweet to the file
        f.append(str(tweet.id) + "\n")
        with open(os.environ['TWEETS_FILE'], "a") as file:
            file.write(str(tweet.id) + "\n")
        # in_reply_to_status_id = ID assigned if tweet is a reply
        # Ignore replies
        if tweet.in_reply_to_status_id is not None:
            continue
        # If this tweet contains one of the keywords
        if any(keyword in tweet.text.lower() for keyword in ["xover", "role","setting"]):
               # Roles
               if " role" in tweet.text.lower():
                   safe = False
                   if " role-safe" in tweet.text.lower():
                       safe = True
                   role = get_role(safe, True)
                   if not role == "":
                            try:
                                logger.info(f"Replying to @{tweet.user.screen_name}")
                                api.update_status(status= "@" + tweet.user.screen_name + " " + role,
                                    in_reply_to_status_id=tweet.id,)
                            except:
                                logger.info("Could not reply @ ROLE")
               # Crossovers
               elif " xover" in tweet.text.lower():
                   if any(keyword in tweet.text.lower() for keyword in [" xover [", " xover-safe ["]):
                       # Characters
                       keyword = "xover-safe" if " xover-safe [" in tweet.text.lower() else "xover"
                       safe = True if " xover-safe [" in tweet.text.lower() else False
                       actors = tweet.text.lower().split(keyword)
                       if len(actors) == 2:
                           actors = actors[1]
                           actors = actors.split("/")
                           if len(actors) == 2: 
                                actor1 = actors[0]
                                actor1 = actor1.replace("[", "").strip()
                                actor2 = actors[1]
                                actor2 = actor2[:actor2.find("]")]
                                character1 = get_xover_character(actor1, safe)
                                if not character1 == "":
                                    character2 = get_xover_character(actor2, safe)
                                    if not character2 == "":
                                        try:
                                            logger.info(f"Replying to @{tweet.user.screen_name}")
                                            api.update_status(status= "@" + tweet.user.screen_name + " " + character1 + "/" + character2,
                                                 in_reply_to_status_id=tweet.id,)
                                        except:
                                            logger.info("Could not reply @ CHARACTER")
                   else:
                       # Fandom
                       fandom = get_xover_fandom()
                       if not fandom == "":
                           try:
                                logger.info(f"Replying to @{tweet.user.screen_name}")
                                api.update_status(status= "@" + tweet.user.screen_name + " " + fandom,
                                    in_reply_to_status_id=tweet.id,)
                           except:
                                logger.info("Could not reply @ FANDOM")
               elif "setting" in tweet.text.lower():
                    safe = True if " setting-safe" in tweet.text.lower() else False
                    setting = get_setting(safe)
                    if not setting == "":
                           try:
                                logger.info(f"Replying to @{tweet.user.screen_name}")
                                api.update_status(status= "@" + tweet.user.screen_name + " " + setting,
                                    in_reply_to_status_id=tweet.id,)
                           except:
                                logger.info("Could not reply @ SETTING")

    return new_since_id

def main():
               api = create_api()
               since_id = 1
               # Check for mentions after every 60 seconds
               while True:
                   since_id = check_mentions(api, since_id)
                   logger.info("Listening")
                   time.sleep(60)

if __name__ == "__main__":
                 main()
