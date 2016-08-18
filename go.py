#!/usr/bin/env python3

import sys
import random
import multiprocessing as mp
from pymongo import MongoClient

if len(sys.argv) != 2:
    print('Usage: python3 go.py <core_number>')
    sys.exit(1)

cores = int(sys.argv[1])

def random_string(length):
    return ''.join([chr(random.randint(ord('a'), ord('z')))
        for i in range(length)])

def insert_records():
    collection = MongoClient().gocrazy.hey

    while True:
        collection.insert_many([{
            'data': random_string(1024),
        } for i in range(10000)])

processes = [mp.Process(target=insert_records) for i in range(cores)]

for p in processes:
    p.start()
