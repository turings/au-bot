import csv
import string
import logging
import os
from source.tools import get_random

logger = logging.getLogger()

# Settings; returns a setting
# Please ignore all the duplication, thx
def get_setting(safe):
    # Import settings.txt
    try:
       setting = ""
       # Until a valid setting has been returned
       while setting == "":
            setting = choose_setting(safe)
    except:
        return ""

    return str(setting)    
    
def choose_setting(safe):
    with open(os.environ['SETTINGS_FILE'], newline='') as f:
            reader = csv.reader(f)
            lst = list(reader)
    # Select random setting
            setting = get_random(lst)
            setting = setting[0]
            if "-ns" in setting.lower():
                if safe: 
                    return ""
                else:
                    setting = setting.replace("-NS", "")

            return setting
