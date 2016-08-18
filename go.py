#!/usr/bin/env python3

import random
import multiprocessing as mp
from pymongo import MongoClient

def random_string(length):
    return ''.join([chr(random.randint(ord('a'), ord('z')))
        for i in range(length)])

def insert_records():
    collection = MongoClient().gocrazy.hey

    while True:
        collection.insert_many([{'data': random_string(64)}
            for i in range(10000)])

processes = [mp.Process(target=insert_records) for i in range(20)]

for p in processes:
    p.start()
