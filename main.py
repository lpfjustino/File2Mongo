from pathlib import Path
import os, os.path

import time
import json

from pymongo import MongoClient
from pymongo.errors import *

# Directory settings
matches_folder = 'F:\RUBoosted\\new_matches\\1'
matches_folder2 = 'F:\RUBoosted\\new_matches\\3'
matches_folder3 = 'F:\RUBoosted\\new_matches\\4'
matches_folder4 = 'F:\RUBoosted\\new_matches\\5'
summoners_folder = 'D:\__NOTE\Documentos\RUBoosted\summoners'


# MongoDB Driver settings
client = MongoClient()
db = client['RUBoosted']

def insert_to_collection(directory, collection):
    pathlist = Path(directory).glob('**/*.txt')
    count = 0
    n_files = len(os.listdir(directory))
    o = open('D:\log'+directory+'.txt', 'a')

    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)

        count += 1
        print(count,'/',n_files,'\t',int(100*count/n_files),'%')

        f = open(path_in_str, 'r')

        match = json.load(f)
        try:
            db[collection].insert_one(match)
            # o.write('Successfully inserted \t'+path_in_str)

        except DuplicateKeyError:
            o.write(collection + ' already contains this document:\t'+path_in_str+'\n')

def print_missing(directory):
        pathlist = Path(directory).glob('**/*.txt')
        for i,path in enumerate(pathlist):
            # because path is object not string
            path_in_str = str(path)

            f = open(path_in_str, 'r')

            if(i%10000 == 0):
                print('\t',i/1000,'%')

            match = json.load(f)
            if 'status' in match:
                print(path)


# insert_to_collection(summoners_folder, 'summoners')

# insert_to_collection(matches_folder, 'matches')
# insert_to_collection(matches_folder2, 'matches')
# insert_to_collection(matches_folder3, 'matches')
# insert_to_collection(matches_folder4, 'matches')

print_missing(matches_folder)
