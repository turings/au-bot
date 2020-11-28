import csv
import string
import logging
from source.tools import get_random
from source.variables import roles_same_file
from source.variables import roles_diff_file

logger = logging.getLogger()

# Role assignments; returns a random role
def get_role(safe, same):
    # Import roles.csv
    if same:
        file = roles_same_file
    else:
        file = roles_diff_file
    try:
       role = ""
       while role == "":
            role = choose_role(safe, file)
    except:
        return ""

    return str(role)    

def choose_role(safe, file):
    with open(file, newline='') as f:
            reader = csv.reader(f)
            lst = list(reader)
    # Select random role
            role = get_random(lst)
            role = role[0]
            if safe: 
                if "-ns" in role.lower():
                    return ""

            return role

    