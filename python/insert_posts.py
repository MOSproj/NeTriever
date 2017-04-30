# !/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from Database import Database
from Facebook import Facebook
from DatabasePost import DatabasePost
from FacebookPost import FacebookPost
from NLP import nlp
from bcolors import bcolors

import time
import sys


def insert_posts():
    config = SafeConfigParser()
    config.read('./config.ini')

    facebook = Facebook()
    db = Database()
    groups = db.get_groups()
    while True:
        try:
            for group in groups:
                print group['name']
                feed = facebook.get_feed(group['id'])
                posts_to_insert = []
                for idx, post in enumerate(feed):
                    print idx
                    post = FacebookPost(post)
                    if not db.is_exists(post.get_id()):
                        post = DatabasePost(post)
                        if not post.is_ignored():
                            nlp.analyse_database_post(post, db.get_category_name_by_id(group['category_id']))
                        posts_to_insert.append(post.get_post())
                print "inserting posts"
                if len(posts_to_insert) > 0:
                    db.insert_post(posts_to_insert)
        except Exception, e:
            print bcolors.fail("something went wrong:")
            print sys.exc_info()[0]
            print e
            time.sleep(120)
            pass

        print bcolors.okeblue("need some sleep")
        time.sleep(30)
        print bcolors.okeblue("starting another loop")


if __name__ == '__main__':
    insert_posts()
