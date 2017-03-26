#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from ConfigParser import SafeConfigParser


class Database:

    def __init__(self):
        self.config = SafeConfigParser()
        self.config.read('./config.ini')

        db_full_path = 'mongodb://'
        if self.config.has_option('db', 'username'):
            db_full_path += self.config.get('db', 'username') + ':' + self.config.get('db', 'password') + '@'
        if self.config.has_option('db', 'dbPath'):
            db_full_path += self.config.get('db', 'dbPath')
        else:
            db_full_path += 'localhost:27017'
        if self.config.has_option('db', 'dbName'):
            db_full_path += '/' + self.config.get('db', 'dbName')

        connection = pymongo.MongoClient(db_full_path)
        self.db = connection[self.config.get('db', 'dbName')]

    def get_db(self):
        return self.db

    def get_categories(self):
        return self.db.categories.find()

    def get_groups(self):
        return self.db.groups.find()

    def insert_post(self, post):
        try:
            self.db.posts2.insert(post)
        except pymongo.errors.DuplicateKeyError, e:
            print e

    def post_id_exists(self, post_id):
        return type(self.db.posts.find_one({"id": post_id})) is dict
