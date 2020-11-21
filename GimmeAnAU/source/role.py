import csv
import string
import logging
from source.tools import get_random
from source.variables import roles_file

logger = logging.getLogger()

# Role assignments; returns a random job role
def get_role():
    # Import roles.csv
    try:
        with open(roles_file, newline='') as f:
            reader = csv.reader(f)
            lst = list(reader)
        # Select random role
            role = get_random(lst)
            role = role[0]
    except:
        return None

    return str(role)
