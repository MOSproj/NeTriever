#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbConnection as database


def if_exists(post_id):
    db = database.get_db()
    return type(db.posts.find_one({"id": post_id})) is dict


if __name__ == '__main__':
    print if_exists(18495189153167192)
