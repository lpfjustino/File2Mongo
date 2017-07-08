from pathlib import Path
import time
import json

from pymongo import MongoClient
from pymongo.errors import *

# Directory settings
matches_folder = 'F:\RUBoosted\\new_matches'
summoners_folder = 'D:\__NOTE\Documentos\RUBoosted\summoners'


# MongoDB Driver settings
client = MongoClient()
db = client['RUBoosted']

def insert_to_collection(directory, collection):
    pathlist = Path(directory).glob('**/*.txt')
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)

        f = open(path_in_str, mode="r")
        match = json.load(f)
        try:
            db[collection].insert_one(match)
            print('Successfully inserted \t', path_in_str)

        except DuplicateKeyError:
            print(collection + ' already contains this document:\t', path_in_str)

insert_to_collection(summoners_folder, 'summoners')
insert_to_collection(matches_folder, 'matches')
