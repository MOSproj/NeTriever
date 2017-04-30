#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from Database import Database
from DatabasePost import DatabasePost
from Facebook import Facebook
from FacebookPost import FacebookPost
from NLP import nlp
import time


def update_posts():
    config = SafeConfigParser()
    config.read('./config.ini')

    facebook = Facebook()
    db = Database()
    posts = db.get_posts()
    while True:
        for post in posts:
            db_post = DatabasePost(post)
            if not db_post.is_ignored():
                try:
                    fb_post = FacebookPost(facebook.get_post(db_post.get_id()))
                    if fb_post.get_updated_time() > db_post.get_updated_time():
                        db_post = DatabasePost(fb_post)
                        nlp.analyse_database_post(db_post, db.get_category_name_by_group_id(db_post.get_group_id()))
                        db.update_post(db_post.get_post(), True)
                        print "post " + str(db_post.get_id()) + " just updated"
                    else:
                        print "post " + str(db_post.get_id()) + " has no updates"
                except Exception, e:
                    if u'Unsupported get request. Object with ID' in e.args[0]:
                        db.delete_post(db_post.get_id())
                        print "post " + str(db_post.get_id()) + " is deleted"
                    else:
                        print e

        print "need some sleep"
        time.sleep(5*60)
        print "starting another loop"


if __name__ == '__main__':
    update_posts()
