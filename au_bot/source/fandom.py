import csv
import string
import logging
import os
from source.tools import get_random

logger = logging.getLogger()

# Fandoms; returns a fandom
def get_crossover_fandom():
    # Import fandoms.txt
    try:
        return choose_fandom()
    except:
        return ""
    
def choose_fandom():
    with open(os.environ['FANDOMS_FILE'], newline='') as f:
            reader = csv.reader(f)
            lst = list(reader)
            # Select random fandom
            fandom = get_random(lst)
            fandom = fandom[0]

            return fandom

    