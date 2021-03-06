#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import pymongo


class Database:

    def __init__(self):
        config = SafeConfigParser()
        config.read('./config.ini')
        username = config.get('db', 'username')
        password = config.get('db', 'password')
        db_path = config.get('db', 'dbPath')
        db_name = config.get('db', 'dbName')
        self.db = self.__get_connection(db_path, db_name, username, password)

    def get_db(self):
        return self.db

    def get_categories(self):
        return list(self.db.categories.find())

    def get_groups(self):
        return list(self.db.groups.find())

    def get_groups_by_category_id(self, id):
        return list(self.db.groups.find({'category_id': id}))

    def get_all_posts(self):
        return list(self.db.posts.find())

    def get_ignored_posts(self):
        return list(self.db.posts.find({'ignore': True}))

    def get_posts(self):
        return list(self.db.posts.find({'ignore': False}))

    def get_post(self, post_id):
        return self.db.posts.find_one({"id": post_id})

    def get_category_id_by_group_id(self, group_id):
        try:
            return self.db.groups.find_one({"id": group_id})['category_id']
        except not pymongo.errors, e:
            print e

    def get_category_name_by_id(self, category_id):
        try:
            return self.db.categories.find_one({"id": category_id})['name']
        except not pymongo.errors, e:
            print e

    def get_category_name_by_group_id(self, group_id):
        return self.get_category_name_by_id(self.get_category_id_by_group_id(group_id))

    def insert_database_posts(self, database_posts):
        try:
            dict_posts = [post.get_post() for post in database_posts]
            self.insert_dict_posts(dict_posts)
        except pymongo.errors.DuplicateKeyError, e:
            print e

    def insert_dict_posts(self, dict_posts):
        try:
            self.db.posts.insert(dict_posts)
        except pymongo.errors.DuplicateKeyError, e:
            print e

    def update_database_post(self, database_post, update=False):
        try:
            self.update_dict_post(database_post.get_post(), update)
        except pymongo.errors, e:
            print e

    def update_dict_post(self, dict_post, update=False):
        try:
            self.db.posts.update({'id': dict_post['id']}, dict_post, update)
        except pymongo.errors, e:
            print e

    def delete_post(self, post_id):
        try:
            self.db.posts.delete_one({"id": post_id})
        except not pymongo.errors, e:
            print e

    def set_ignore(self, post_id):
        self.db.posts.save({'id': post_id}, {
            'id': post_id,
            'ignore': True
        })

    def is_exists(self, post_id):
        return isinstance(self.db.posts.find_one({"id": post_id}), dict)

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
