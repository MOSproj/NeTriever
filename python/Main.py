#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from Facebook import Facebook
from Database import Database
from datetime import datetime


class Main:

    def __init__(self):
        config = SafeConfigParser()
        config.read('./config.ini')

        self.facebook = Facebook(config.get('facebook', 'access_token'))
        self.db = self.__connect_to_db(config)

    def filter_posts(self, feed):
        new_posts = []
        updated_posts = []
        for post in feed:
            if not post['is_expired'] and not post['is_hidden']:
                post_id = long(post['id'].split("_")[1])
                if self.db.if_exists(post_id):
                    updated_posts.append(post)
                else:
                    new_posts.append(post)
            else:
                self.db.set_ignore(post['id'])
        return new_posts, updated_posts

    def get_data_from_post(self, post):
        post_data = dict()
        post_data['id'] = long(post['id'].split("_")[1])
        post_data['group_id'] = long(post['id'].split("_")[0])
        post_data['from'] = {
            'name': post['from']['name'],
            'id': long(post['from']['id'])
        }
        post_data['created_time'] = datetime.strptime(post['created_time'], "%Y-%m-%dT%H:%M:%S+%f")
        post_data['last_updated'] = datetime.utcnow()
        # TODO: insert "NLP" here
        if 'message' in post:
            post_data['message'] = post['message']
        if 'attachments' in post:
            post_data['image'] = []
            data_array = post['attachments']['data'][0]['subattachments']['data']
            for data in data_array:
                post_data['image'].append(data['media']['image'])
        post_data['ignore'] = False
        return post_data

    def new_and_updated(self, posts):
        new_posts = []
        updated_posts = []
        for post in posts:
            post_id = long(post['id'].split("_")[1])
            if self.db.if_exists(post_id):
                    updated_posts.append(post)
                    new_posts.append(post)
        return new_posts, updated_posts

    def ignore_or_not(self, posts):
        not_ignore = []
        ignore = []
        for post in posts:
            if not post['is_expired'] and not post['is_hidden']:
                not_ignore.append(post)
            else:
                ignore.append(post)
        return not_ignore, ignore

    def __connect_to_db(self, config):
        if config.has_option('db', 'username'):
            username = config.get('db', 'username')
            password = config.get('db', 'password')
        else:
            username = ''
            password = ''

        if config.has_option('db', 'dbPath'):
            db_path = config.get('db', 'dbPath')
        else:
            db_path = 'localhost:27017'

        if config.has_option('db', 'dbName'):
            db_name = config.get('db', 'dbName')
        else:
            db_name = ''

        return Database(db_path, db_name, username, password)
