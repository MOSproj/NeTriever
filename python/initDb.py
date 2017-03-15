#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from initDb import init_categories, init_groups, init_posts
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

categories = [{
    "name": "רכב"
}, {
    "name": "סלולר"
}, {
    "name": "נדלן"
}]

groups = [{
    "id": 34704043320127,
    "facebook_name": "pishpeshuk.cars",
    "name": "פשפשוק רכב",
    "category": "רכב"
}, {
    "id": 1555004694768144,
    "name": "פשפשוק סלולר",
    "category": "סלולר"
}, {

    "id": 303803599700653,
    "facebook_name": "pishpeshuk.Nadlan",
    "name": "פשפשוק נדלן",
    "category": "נדלן"
}]

init_categories(db, categories)
init_groups(db, groups)
init_posts(db)
