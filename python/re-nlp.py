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


db = Database()
facebook = Facebook()

posts = db.get_posts()
for post in posts:
    db_post = DatabasePost(post)
    try:
        fb_post = FacebookPost(facebook.get_post(db_post.get_id()))
        db_post = DatabasePost(fb_post)
        nlp.analyse_database_post(db_post, db.get_category_name_by_group_id(db_post.get_group_id()))
        db.update_database_post(db_post, True)
        print "post " + str(db_post.get_id()) + " just updated"
    except Exception, e:
        if u'Unsupported get request. Object with ID' in e.args[0]:
            db.delete_post(db_post.get_id())
            print "post " + str(db_post.get_id()) + " is deleted"
        else:
            print e
