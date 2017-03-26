#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbConnection as database


def get_categories():
    db = database.get_db()
    return db.categories.find()


if __name__ == '__main__':
    for category in get_categories():
        print category
