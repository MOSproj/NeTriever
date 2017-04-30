#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from Database import Database
from DatabasePost import DatabasePost
import time
import datetime


def delete_ignore():
    config = SafeConfigParser()
    config.read('./config.ini')

    db = Database()
    posts = db.get_posts()
    while True:
        for post in posts:
            db_post = DatabasePost(post)
            if db_post.is_ignored():
                if (db_post.get_last_updated() - datetime.datetime.now()).days < -10:
                    db.delete_post(db_post.get_id())
                    print "post " + str(db_post.get_id()) + " is deleted - is ignore for a month"
                else:
                    print "post " + str(db_post.get_id()) + " is ignored"

        print "need some sleep"
        time.sleep(5*60)
        print "starting another loop"


if __name__ == '__main__':
    delete_ignore()
