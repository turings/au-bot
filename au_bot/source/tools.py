import requests
import random
import json
import datetime

# Get a random item from the list
def get_random(items):
        return items[random.randint(0, len(items) - 1)]

# Get json from response
def get_json(end_point):
        res = requests.get(end_point)
        jso = json.loads(res.text)

        return jso

# String -> date
def get_date(str):
    if isinstance(str, datetime.date):
        return str
    return datetime.datetime.strptime(str, '%Y-%m-%d')

# Create file
def create_file(file_name):
    try:
        f = open(file_name)
    except:
        f = open(file_name)
        f.close()
