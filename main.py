from pathlib import Path
import os, os.path

import time
import json

from pymongo import MongoClient
from pymongo.errors import *

# Directory settings
matches_folder = 'F:\RUBoosted\\new_matches\\1'
matches_folder2 = 'F:\RUBoosted\\new_matches\\2'
matches_folder3 = 'F:\RUBoosted\\new_matches\\3'
matches_folder4 = 'F:\RUBoosted\\new_matches\\4'
matches_folder5 = 'F:\RUBoosted\\new_matches\\5'
matches_folder6 = 'F:\RUBoosted\\new_matches\\6'
matches_folder7 = 'F:\RUBoosted\\new_matches\\7'
matches_folder8 = 'F:\RUBoosted\\new_matches\\8'
matches_folder9 = 'F:\RUBoosted\\new_matches\\9'
matches_folder10 = 'F:\RUBoosted\\new_matches\\10'
matches_folder11 = 'F:\RUBoosted\\new_matches\\11'
matches_folder12 = 'F:\RUBoosted\\new_matches\\12'
matches_folder13 = 'F:\RUBoosted\\new_matches\\13'
matches_folder14 = 'F:\RUBoosted\\new_matches\\14'
matches_folder15 = 'F:\RUBoosted\\new_matches\\15'
matches_folder16 = 'F:\RUBoosted\\new_matches\\16'
matches_folder17 = 'F:\RUBoosted\\new_matches\\17'
matches_folder18 = 'F:\RUBoosted\\new_matches\\18'
matches_foldera = 'F:\RUBoosted\\new_matches\\a'
matches_folderb = 'F:\RUBoosted\\new_matches\\b'
matches_folderc = 'F:\RUBoosted\\new_matches\\c'
matches_folderd = 'F:\RUBoosted\\new_matches\\d'
matches_foldere = 'F:\RUBoosted\\new_matches\\e'
matches_folderf = 'F:\RUBoosted\\new_matches\\f'
matches_folderg = 'F:\RUBoosted\\new_matches\\g'
matches_folderh = 'F:\RUBoosted\\new_matches\\h'
matches_folderi = 'F:\RUBoosted\\new_matches\\i'
matches_folderj = 'F:\RUBoosted\\new_matches\\j'
matches_folderk = 'F:\RUBoosted\\new_matches\\k'
matches_folderl = 'F:\RUBoosted\\new_matches\\l'
matches_folderm = 'F:\RUBoosted\\new_matches\\m'
matches_foldern = 'F:\RUBoosted\\new_matches\\n'

summoners_folder = 'D:\__NOTE\Documentos\RUBoosted\summoners'

missing = 'C:\\Users\LuisPaulo\Documents\GitHub\RUBoosted\matches'


# MongoDB Driver settings
client = MongoClient()
db = client['RUBoosted']

def insert_to_collection(directory, collection, temp):
    pathlist = Path(directory).glob('**/*.txt')
    count = 0
    n_files = len(os.listdir(directory))
    s = open('D:\success'+temp+'.txt', 'a')
    e = open('D:\\failure'+temp+'.txt', 'a')

    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)

        count += 1
        print(count,'/',n_files,'\t',int(100*count/n_files),'%')

        f = open(path_in_str, 'r')

        match = json.load(f)
        try:
            db[collection].insert_one(match)
            s.write(str(gameid_from_path(path))+'\n')

        except DuplicateKeyError:
            e.write(str(gameid_from_path(path))+'\n')
            pass

def print_missing(directory):
        ids = []
        pathlist = Path(directory).glob('**/*.txt')
        for i,path in enumerate(pathlist):
            # because path is object not string
            path_in_str = str(path)

            f = open(path_in_str, 'r')

            if(i%10000 == 0):
                print('\t',i/1000,'%')

            match = json.load(f)
            if 'status' in match:
                ids.append(gameid_from_path(path)) # GameID from directory
                print(ids)

def gameid_from_path(path):
    return int(str.split(str.split(str(path), '\\')[4], '.')[0])

# insert_to_collection(summoners_folder, 'summoners')

# insert_to_collection(matches_folder, 'matches', '1')
# insert_to_collection(matches_folder2, 'matches', '2')
# insert_to_collection(matches_folder3, 'matches', '3')
# insert_to_collection(matches_folder4, 'matches', '4')
# insert_to_collection(matches_folder5, 'matches', '5')
# insert_to_collection(matches_folder6, 'matches', '6')
# insert_to_collection(matches_folder7, 'matches', '7')
# insert_to_collection(matches_folder8, 'matches', '8')
# insert_to_collection(matches_folder9, 'matches', '9')
# insert_to_collection(matches_folder10, 'matches', '10')
# insert_to_collection(matches_folder11, 'matches', '11')
# insert_to_collection(matches_folder12, 'matches', '12')
# insert_to_collection(matches_folder13, 'matches', '13')
# insert_to_collection(matches_folder14, 'matches', '14')
# insert_to_collection(matches_folder15, 'matches', '15')
# insert_to_collection(matches_folder16, 'matches', '16')
# insert_to_collection(matches_folder17, 'matches', '17')
# insert_to_collection(matches_folder18, 'matches', '18')
# insert_to_collection(matches_foldera, 'matches', 'a')
# insert_to_collection(matches_folderb, 'matches', 'b')
# insert_to_collection(matches_folderd, 'matches', 'd')
# insert_to_collection(matches_foldere, 'matches', 'e')
# insert_to_collection(matches_folderf, 'matches', 'f')
# insert_to_collection(matches_folderg, 'matches', 'g')
# insert_to_collection(matches_folderh, 'matches', 'h')

# insert_to_collection(matches_folderi, 'matches', 'i')
# insert_to_collection(matches_folderj, 'matches', 'j')
# insert_to_collection(matches_folderk, 'matches', 'k')
# insert_to_collection(matches_folderl, 'matches', 'l')
# insert_to_collection(matches_folderm, 'matches', 'm')
# insert_to_collection(matches_foldern, 'matches', 'n')

# insert_to_collection(missing, 'matches', 'temp')

# print_missing(matches_foldern)
# print('n')
