import tweepy
import logging
import time
import string
from source.config import create_api
from source.tools import create_file
from source.role import get_role
from source.character import get_crossover_character
from source.variables import tweets_file
from source.variables import my_username

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("loading")
    create_file(tweets_file)
    f = open(tweets_file, "r").readlines()
    logger.info("getting mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        if str(tweet.id) + "\n" in f:
            continue
        new_since_id = max(tweet.id, new_since_id)
        logger.info("recording tweet id")
        f.append(tweet.id)
        with open(tweets_file, "a") as file:
            file.write(str(tweet.id) + "\n")
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
               logger.info(f"replying to @{tweet.user.screen_name}")
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
                        actor1 = actor1.replace(my_username + " " + keyword + " ", "")
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
               while True:
                   since_id = check_mentions(api, ["role", "crossover"], since_id)
                   logger.info("listening")
                   time.sleep(60)

if __name__ == "__main__":
                 main()
