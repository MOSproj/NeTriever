#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbConnection as database


def get_groups():
    db = database.get_db()
    return db.groups.find()


if __name__ == '__main__':
    for group in get_groups():
        print group
