# !/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from Database import Database
from Facebook import Facebook
from DatabasePost import DatabasePost
from FacebookPost import FacebookPost
from NLP import nlp
import time
import sys


def main():
    config = SafeConfigParser()
    config.read('./config.ini')

    facebook = Facebook(config)
    db = Database(config)
    groups = list(db.get_groups())
    while True:
        try:
            for group in groups:
                print group['name']
                feed = facebook.get_feed(group['id'])
                posts_to_insert = []
                for idx, post in enumerate(feed):
                    print idx
                    post = DatabasePost(post)
                    if not db.is_exists(post.get_id()):
                        if not post.is_ignored():
                            nlp.analyse_database_post(post, db.get_category_name_by_id(group['category_id']))
                        posts_to_insert.append(post.get_post())
                print "inserting posts"
                if len(posts_to_insert) > 0:
                    db.insert_post(posts_to_insert)
        except Exception, e:
            print "something went wrong:"
            print sys.exc_info()[0]
            print e
            time.sleep(120)
            pass

        print "need some sleep"
        time.sleep(30)
        print "starting another loop"


if __name__ == '__main__':
    main()
