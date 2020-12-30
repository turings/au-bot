import csv
import string
import logging
import os
from source.tools import get_random

logger = logging.getLogger()

# Role assignments; returns a random role
def get_role(safe, same):
    # Import roles.txt
    try:
       role = ""
       # Until a valid role has been returned
       while role == "":
            role = choose_role(safe)
    except:
        return ""

    return str(role)    

def choose_role(safe):
    with open(os.environ['ROLES_FILE'], newline='') as f:
            reader = csv.reader(f)
            lst = list(reader)
    # Select random role
            role = get_random(lst)
            role = role[0]
            if "-ns" in role.lower():
                if safe: 
                    return ""
                else:
                    role = role.replace("-NS", "")

            return role

    