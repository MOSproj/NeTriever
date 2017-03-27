#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo


class Database:

    def __init__(self, db_path, db_name, username, password):
        self.db = self.__get_connection(db_path, db_name, username, password)

    def get_db(self):
        return self.db

    def get_categories(self):
        return self.db.categories.find()

    def get_groups(self):
        return self.db.groups.find()

    def get_post(self, post_id):
        return self.db.posts.find_one({"id": post_id})

    def insert_post(self, post):
        try:
            self.db.posts2.insert(post)
        except pymongo.errors.DuplicateKeyError, e:
            print e

    def __get_connection(self, db_path, db_name, username, password):
        db_full_path = 'mongodb://'
        if len(username) > 0:
            db_full_path += username + ':' + password + '@'
        db_full_path += db_path
        if len(db_name) > 0:
            db_full_path += '/' + db_name

        connection = pymongo.MongoClient(db_full_path)
        return connection[db_name]
