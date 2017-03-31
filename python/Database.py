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
            self.db.posts.insert(post)
        except pymongo.errors.DuplicateKeyError, e:
            print e

    def update_post(self, post, update=False):
        try:
            self.db.posts.update({'id': post['id']}, post, update)
        except pymongo.errors, e:
            print e

    def set_ignore(self, post_id):
        self.db.posts.save({"id": post_id}, {
            "id": post_id,
            "ignore": True
        })

    def if_exists(self, post_id):
        return type(self.db.posts.find_one({"id": post_id})) is dict

    def __get_connection(self, db_path, db_name, username, password):
        uri = 'mongodb://'
        if len(username) > 0:
            uri += username + ':' + password + '@'
        if len(db_path) > 0:
            uri += db_path
        else:
            uri += 'localhost:27017'

        connection = pymongo.MongoClient(uri)
        return connection[db_name]
