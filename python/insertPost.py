#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
import pprint
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('./config.ini')

dbFullPath = 'mongodb://'
if config.has_option('db', 'username'):
    dbFullPath += config.get('db', 'username') + ':' + config.get('db', 'password') + '@'
if config.has_option('db', 'dbPath'):
    dbFullPath += config.get('db', 'dbPath')
else:
    dbFullPath += 'localhost:27017'
if config.has_option('db', 'dbName'):
    dbFullPath += '/' + config.get('db', 'dbName')

connection = pymongo.MongoClient(dbFullPath)
db = connection[config.get('db', 'dbName')]

post = {
    "id": "134704043320127_623147004475826",
    "from": {
        "name": "רון אזולאי",
        "id": "992406777436668"
    },
    "price": "4999",
    "phone": "0545485497",
    "specifications": [
        {
            "name": "שנה",
            "value": "2003"
        },
        {
            "name": "חברה",
            "value": "אופל"
        },
        {
            "name": "דגם",
            "value": "קורסה"
        },
        {
            "name": "יד",
            "value": "3"
        },
        {
            "name": "קילומטר",
            "value": "200"
        },
        {
            "name": "גיר",
            "value": "רובוטי"
        }
    ]
}

try:
    db.posts.insert(post)
except pymongo.errors.DuplicateKeyError, e:
    print e
