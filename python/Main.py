#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from Database import Database
from Facebook import Facebook
from DatabasePost import DatabasePost
from FacebookPost import FacebookPost
from NLP import NLP
import time


def main():
    config = SafeConfigParser()
    config.read('./config.ini')

    facebook = Facebook(config.get('facebook', 'access_token'))
    db = connect_to_db(config)
    categories = list(db.get_categories())
    groups = list(db.get_groups())

    for group in groups:
        for category in categories:
            if group['category'].id == category['_id']:
                group['category_name'] = category['name']
                break
    while True:
        try:
            for group in groups:
                print group['name']
                feed = facebook.get_feed(group['id'])

                posts_to_insert = []
                posts_to_update = []
                for idx, post in enumerate(feed):
                    print idx
                    post = DatabasePost(post)
                    post_from_db = db.get_post(post.get_id())
                    if isinstance(post_from_db, dict):
                        post_from_db = DatabasePost(post_from_db)
                        if not post_from_db.is_ignored() and post.get_updated_time() > post_from_db.get_updated_time():
                            if not post.is_ignored():
                                NLP.analyse_database_post(post, group['category_name'])
                            posts_to_update.append(post.get_post())
                    else:
                        if not post.is_ignored():
                            NLP.analyse_database_post(post, group['category_name'])
                        posts_to_insert.append(post.get_post())
                print "inserting posts"
                if len(posts_to_insert) > 0:
                    db.insert_post(posts_to_insert)
                for post in posts_to_update:
                    db.update_post(post, True)
        except Exception, e:
            print "something went wrong:"
            print e
            time.sleep(120)
            pass

        print "need some sleep"
        time.sleep(30)
        print "starting another loop"


def connect_to_db(config):
    username = config.get('db', 'username')
    password = config.get('db', 'password')
    db_path = config.get('db', 'dbPath')
    db_name = config.get('db', 'dbName')

    return Database(db_path, db_name, username, password)


if __name__ == '__main__':
    main()
