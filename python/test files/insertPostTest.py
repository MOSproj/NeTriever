#!/usr/bin/env python
# -*- coding: utf-8 -*-
from python.database.dbConnection import *
import datetime
from bson.dbref import DBRef
import python.database
import python.Database


def main(database):
    post = {
        "id": 623147004475826,
        "group": DBRef(collection="groups", id="group id.."),
        "from": {
            "name": "רון אזולאי",
            "id": 992406777436668
        },
        "price": "4999",
        "phone": "0545485497",
        "message": "...",
        "link": "link..",
        "created_time": datetime.datetime.utcnow(),
        "updated_time": datetime.datetime.utcnow(),
        "images": [{
            "height": 720,
            "src": "src..",
            "width": 405
        }],
        "ignore": False,
        "specs": {
            "שנה": 2003,
            "חברה": "אופל",
            "דגם": "קורסה",
            "יד": "3",
            "קילומטר": "200",
            "גיר": "רובוטי"
        }
    }

    database.insert_post(post)

if __name__ == '__main__':
    database = python.Database.Database()
    main(database)
