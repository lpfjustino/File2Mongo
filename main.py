from pathlib import Path
import time
import json

from pymongo import MongoClient

# Directory settings
directory = 'F:\RUBoosted\\new_matches'
pathlist = Path(directory).glob('**/*.txt')

# MongoDB Driver settings
client = MongoClient()
db = client['RUBoosted']

for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)

    with open(path_in_str, mode="r") as f:
        match = json.load(f)
        db.matches.insert_one(match)

        time.sleep(10)
