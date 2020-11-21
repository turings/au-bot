import string
import logging
import datetime
from source.tools import get_random
from source.tools import get_json
from source.tools import get_date
from dateutil.relativedelta import relativedelta
from source.variables import movie_end_point
from source.variables import movie_key

logger = logging.getLogger()
invalidnames = ['self', 
                'himself', 
                'herself', 
                'themselves', 
                '(voice)', 
                'voice', 
                '']

# Crossover; returns film/tv character based on actor name
def get_crossover_character(actor_name):
    # Use character class to get a character
    char = character()
    if char.get_character(actor_name):
        return char.character_name + " (" + char.film_name + ")"
    else:
        return ""

class character:
    global character_name
    global film_name
    actor_id = 0
    actor_dob = datetime.datetime(1, 1, 1)
    film_date = datetime.datetime(1, 1, 1)
    searches = 0

    def get_character(self, actor_name):
        if self.get_actor(actor_name):
            if self.get_dob():
                if self.get_credit():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def get_actor(self, actor_name):
        try:
            actor_name = actor_name.replace(" ", "%2B")
            end_point = movie_end_point + "/search/person?api_key=" + movie_key + "&language=en-US&query=" + actor_name
            # Search for actor, find ID
            r = get_json(end_point)
            i = r["results"][0]
            self.actor_id = i["id"]
            if self.actor_id == 0:
                return False
            return True
        except:
            return False

    def get_dob(self):
        try:
            end_point = movie_end_point + "/person/" + str(self.actor_id) + "?api_key=" + movie_key + "&language=en-US"
            # Use ID to find actor record
            r = get_json(end_point)
            self.actor_dob = r["birthday"]
            return True
        except:
            return False

    def get_credit(self):
        end_point = movie_end_point + "/person/" + str(self.actor_id) + "/combined_credits?api_key=" + movie_key + "&language=en-US"
        # User ID to get random credit
        credits = get_json(end_point)
        credits = credits["cast"]
        credit = get_random(credits)
        # Get character name
        self.character_name = credit["character"]
        # Work out other attributes based on TV/film
        media_type = credit["media_type"]
        if media_type == "tv":
            self.film_name = credit["original_name"]
            self.film_date = credit["first_air_date"]
        else:
            self.film_name = credit["original_title"]
            self.film_date = credit["release_date"]
        if not self.check_valid():
            if self.searches > 20:
               # Couldn't find a valid record; give up
               return False
            # Run this until we find an over 17 credit
            self.searches += 1
            self.get_credit()
         
        return True           

    # Make sure that the actor was over 17 when this film was released
    def over_17(self):
        diff = relativedelta(self.film_date, self.actor_dob)
        if diff.years > 17:
            return True
        else:
            return False

    # Validity checks
    def check_valid(self):
        try:
            self.actor_dob = get_date(self.actor_dob)
            self.film_date = get_date(self.film_date)
        except:
            return False
        if not self.over_17():
            return False
        if self.character_name.lower() in invalidnames:
            return False
        return True