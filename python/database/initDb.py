#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from bson.dbref import DBRef
import dbConnection


def init_categories(db, categories=[]):
    try:
        db.create_collection("categories")
        db.categories.create_index([("name", pymongo.ASCENDING)], unique=True)
    except pymongo.errors.CollectionInvalid:
        print "pymongo.errors.CollectionInvalid: categories"
        pass

    for category in categories:
        try:
            db.categories.insert(category)
        except pymongo.errors.DuplicateKeyError:
            print "pymongo.errors.DuplicateKeyError: " + category["name"] + " category"
            pass


def init_groups(db, groups=[]):
    try:
        db.create_collection("groups")
        db.groups.create_index([("id", pymongo.ASCENDING)], unique=True)
    except pymongo.errors.CollectionInvalid:
        print "pymongo.errors.CollectionInvalid: groups"
        pass

    for group in groups:
        try:
            cat_id = db.categories.find_one({"name": group["category"]})
            group["category"] = DBRef(collection="categories", id=cat_id["_id"])
            db.groups.insert(group)
        except pymongo.errors.DuplicateKeyError:
            print "pymongo.errors.DuplicateKeyError: " + group["name"]
            pass


def init_posts(db, posts=[]):
    try:
        db.create_collection("posts")
        db.posts.create_index([("id", pymongo.ASCENDING)], unique=True)
    except pymongo.errors.CollectionInvalid:
        print "pymongo.errors.CollectionInvalid: posts"
        pass

    for post in posts:
        try:
            group_id = db.groups.find_one({"id": post["group"]})
            post["group"] = DBRef(collection="groups", id=group_id["_id"])
            db.posts.insert(post)
        except pymongo.errors.DuplicateKeyError:
            print "pymongo.errors.DuplicateKeyError: " + post["id"]
            pass


def main():
    categories = [{
        "name": "רכב",
        "specs": {
            "חברה": ["יונדאי", "מרצדס"],
            "שנה": "1990-2017",
            "יד": "0-10",
            "מחיר": "1-5000000",
            "קמ": "0-600000",
        }
    }, {
        "name": "סלולר",
        "specs": {
            "יצרן": ["samsung", "LG"],
            "אזור": ["באר שבע", "תל אביב"],
            "זיכרון": ["32", "64"]
        }
    }, {
        "name": "נדלן",
        "specs": {
            "סטאטוס": ["מכירה", "השכרה"],
            "מחיר": "1-5000000",
            "אזור": ["באר שבע", "תל אביב"],
            "גודל במר ": "1-600000",
            "מס חדרים": "1-20"
        }
    }]

    groups = [{
        "id": 134704043320127,
        "facebook_name": "pishpeshuk.cars",
        "name": "פשפשוק רכב",
        "category": "רכב"
    }, {
        "id": 1555004694768144,
        "name": "פשפשוק סלולר",
        "category": "סלולר"
    }, {

        "id": 303803599700653,
        "facebook_name": "pishpeshuk.Nadlan",
        "name": "פשפשוק נדלן",
        "category": "נדלן"
    }]

    db = dbConnection.get_db()

    init_categories(db, categories)
    init_groups(db, groups)
    init_posts(db)


if __name__ == '__main__':
    main()
