#!/usr/bin/env python
import os.path
import pymongo
from ConfigParser import SafeConfigParser


def get_db():
    config = SafeConfigParser()
    if os.path.exists('./config.ini'):
        config.read('./config.ini')
    else:
        config.read('./../config.ini')

    db_full_path = 'mongodb://'
    if config.has_option('db', 'username'):
        db_full_path += config.get('db', 'username') + ':' + config.get('db', 'password') + '@'
    if config.has_option('db', 'dbPath'):
        db_full_path += config.get('db', 'dbPath')
    else:
        db_full_path += 'localhost:27017'
    if config.has_option('db', 'dbName'):
        db_full_path += '/' + config.get('db', 'dbName')

    connection = pymongo.MongoClient(db_full_path)
    return connection[config.get('db', 'dbName')]

if __name__ == '__main__':
    print get_db()
