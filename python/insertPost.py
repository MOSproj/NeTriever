#!/usr/bin/env python
# -*- coding: utf-8 -*-
from python.database.dbConnection import *
import database


def main():
    post = {
        "id": "134704043320127_623147004475826",
        "from": {
            "name": "רון אזולאי",
            "id": "992406777436668"
        },
        "price": "4999",
        "phone": "0545485497",
        "specifications": [
            {
                "name": "שנה",
                "value": "2003"
            },
            {
                "name": "חברה",
                "value": "אופל"
            },
            {
                "name": "דגם",
                "value": "קורסה"
            },
            {
                "name": "יד",
                "value": "3"
            },
            {
                "name": "קילומטר",
                "value": "200"
            },
            {
                "name": "גיר",
                "value": "רובוטי"
            }
        ]
    }

    db = database.get_db()

    try:
        db.posts.insert(post)
    except pymongo.errors.DuplicateKeyError, e:
        print e

if __name__ == '__main__':
    main()
