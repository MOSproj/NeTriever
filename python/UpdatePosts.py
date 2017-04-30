# !/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

from Database import Database
from Facebook import Facebook
from DatabasePost import DatabasePost
from FacebookPost import FacebookPost
from NLP import nlp
from bcolors import bcolors


class UpdatePosts(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval

        self.db = Database()
        self.facebook = Facebook()

    def run(self):
        while True:
            self.update_posts()
            print bcolors.okeblue("need some sleep")
            time.sleep(self.interval)
            print bcolors.okeblue("starting another loop")

    def update_posts(self):
        posts = self.db.get_posts()
        for post in posts:
            db_post = DatabasePost(post)
            try:
                fb_post = FacebookPost(self.facebook.get_post(db_post.get_id()))
                if fb_post.get_updated_time() > db_post.get_updated_time():
                    db_post = DatabasePost(fb_post)
                    nlp.analyse_database_post(db_post, self.db.get_category_name_by_group_id(db_post.get_group_id()))
                    self.db.update_database_post(db_post, True)
                    print "post " + str(db_post.get_id()) + " just updated"
                else:
                    print "post " + str(db_post.get_id()) + " has no updates"
            except Exception, e:
                if u'Unsupported get request. Object with ID' in e.args[0]:
                    self.db.delete_post(db_post.get_id())
                    print "post " + str(db_post.get_id()) + " is deleted"
                else:
                    print e
