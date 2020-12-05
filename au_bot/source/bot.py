import tweepy
import logging
import time
import string
import os
from source.config import create_api
from source.tools import create_file
from source.role import get_role
from source.character import get_crossover_character

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
        if str(tweet.id) + "\n" in f:
            continue
        logger.info("recording tweet id")
        # Add this tweet to the file
        f.append(str(tweet.id) + "\n")
        with open(os.environ['TWEETS_FILE'], "a") as file:
            file.write(str(tweet.id) + "\n")
        # in_reply_to_status_id = ID assigned if tweet is a reply
        # Ignore replies
        if tweet.in_reply_to_status_id is not None:
            continue
        # If this tweet contains one of the keywords
        if any(keyword in tweet.text.lower() for keyword in ["crossover", "role"]):
               logger.info(f"Replying to @{tweet.user.screen_name}")
               # Roles
               if "rolesame" in tweet.text.lower():
                   safe = False
                   if "rolesame-safe" in tweet.text.lower():
                       safe = True
                   role = get_role(safe, True)
                   if not role == "":
                            api.update_status(status= "@" + tweet.user.screen_name + " " + role,
                                in_reply_to_status_id=tweet.id,)
               elif "rolediff" in tweet.text.lower():
                   safe = False
                   if "rolediff-safe" in tweet.text.lower():
                       safe = True
                   role1 = get_role(safe, False)
                   if not role1 == "":
                       role2 = get_role(safe, False)
                       if not role2 == "":
                            api.update_status(status= "@" + tweet.user.screen_name + " " + role1 + "/" + role2,
                                in_reply_to_status_id=tweet.id,)
               # Crossovers
               elif "crossover" in tweet.text.lower():
                   keyword = "crossover"
                   safe = False
                   if "crossover-safe" in tweet.text.lower():
                        keyword = "crossover-safe"
                        safe = True
                   actors = tweet.text.lower().split("/")
                   if len(actors) == 2: 
                        actor1 = actors[0]
                        actor2 = actors[1]
                        actor1 = actor1.replace("@" + os.environ['MY_USERNAME'] + " " + keyword + " ", "")
                        character1 = get_crossover_character(actor1, safe)
                        if not character1 == "":
                            character2 = get_crossover_character(actor2, safe)
                            if not character2 == "":
                                api.update_status(status= "@" + tweet.user.screen_name + " " + character1 + "/" + character2,
                                     in_reply_to_status_id=tweet.id,)

    return new_since_id

def main():
               api = create_api()
               since_id = 1
               # Check for mentions after every 60 seconds
               while True:
                   since_id = check_mentions(api, since_id)
                   logger.info("listening")
                   time.sleep(60)

if __name__ == "__main__":
                 main()
