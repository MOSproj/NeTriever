# !/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
import sys

from Database import Database
from Facebook import Facebook
from DatabasePost import DatabasePost
from FacebookPost import FacebookPost
from NLP import nlp
from bcolors import bcolors


class InsertPosts(threading.Thread):
    def __init__(self, category_name, groups, interval):
        threading.Thread.__init__(self)
        self.category_name = category_name
        self.groups = groups
        self.interval = interval

        self.db = Database()
        self.facebook = Facebook()

    def run(self):
        while True:
            self.insert_posts()
            print bcolors.okeblue("need some sleep")
            time.sleep(self.interval)
            print bcolors.okeblue("starting another loop")

    def insert_posts(self):
        try:
            for group in self.groups:
                print group['name']
                feed = self.facebook.get_feed(group['id'])
                posts_to_insert = []
                for idx, post in enumerate(feed):
                    print idx
                    post = FacebookPost(post)
                    if not self.db.is_exists(post.get_id()):
                        post = DatabasePost(post)
                        if not post.is_ignored():
                            nlp.analyse_database_post(post, self.db.get_category_name_by_id(group['category_id']))
                        posts_to_insert.append(post)
                print "inserting posts"
                if len(posts_to_insert) > 0:
                    self.db.insert_database_posts(posts_to_insert)
        except Exception, e:
            print bcolors.fail("something went wrong:")
            print sys.exc_info()[0]
            print e
            time.sleep(120)
            pass
