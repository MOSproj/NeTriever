#!/usr/bin/env python
# -*- coding: utf-8 -*-
from python.database.dbConnection import *
import datetime
from bson.dbref import DBRef
import python.database


def insert_post(post):
    db = python.database.get_db()

    try:
        db.posts2.insert(post)
    except pymongo.errors.DuplicateKeyError, e:
        print e

if __name__ == '__main__':
    insert_post({})
