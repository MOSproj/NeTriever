# !/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
from datetime import datetime

from Database import Database
from Facebook import Facebook
from DatabasePost import DatabasePost
from bcolors import bcolors


class DeleteIgnore(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval

        self.db = Database()
        self.facebook = Facebook()

        self.days_to_delete_interval = 7

    def run(self):
        while True:
            self.delete_ignore()
            print bcolors.okeblue("need some sleep")
            time.sleep(self.interval)
            print bcolors.okeblue("starting another loop")

    def delete_ignore(self):
        posts = self.db.get_ignored_posts()
        for post in posts:
            db_post = DatabasePost(post)
            if (db_post.get_last_updated() - datetime.now()).days < - self.days_to_delete_interval:
                self.db.delete_post(db_post.get_id())
                print "post " + str(db_post.get_id()) + " is deleted - is ignore interval"
            else:
                print "post " + str(db_post.get_id()) + " is ignored"
