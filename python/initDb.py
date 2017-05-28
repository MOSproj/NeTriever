#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from bson.dbref import DBRef
import python.Database
from python.Database import Database


# TODO: this file is broken
def init_categories(db, categories=[]):
    try:
        db.create_collection("categories")
        db.categories.create_index([("id", pymongo.ASCENDING)], unique=True)
        db.categories.create_index([("name", pymongo.ASCENDING)], unique=True)
    except pymongo.errors.CollectionInvalid, e:
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
        db.groups.create_index([("category_id", pymongo.ASCENDING)], unique=False)
        db.groups.create_index([("id", pymongo.ASCENDING)], unique=True)
        db.groups.create_index([("name", pymongo.ASCENDING)], unique=True)
    except pymongo.errors.CollectionInvalid:
        print "pymongo.errors.CollectionInvalid: groups"
        pass

    for group in groups:
        try:
            db.groups.insert(group)
        except pymongo.errors.DuplicateKeyError:
            print "pymongo.errors.DuplicateKeyError: " + group["name"]
            pass


def init_posts(db, posts=[]):
    try:
        db.create_collection("posts")
        db.posts.create_index([("updated_time", pymongo.ASCENDING)], unique=False)
        db.posts.create_index([("id", pymongo.ASCENDING)], unique=True)
        db.posts.create_index([("group_id", pymongo.ASCENDING)], unique=False)
        db.posts.create_index([("ignore", pymongo.ASCENDING)], unique=False)
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


def main(database):
    categories = [{
        "id": 3,
        "name": "נדלן",
        "specs": {
            "מכירה \\ השכרה": [
                "מכירה",
                "השכרה"
            ],
            "סוג": [
                "שותפים",
                "תיווך",
                "סאבלט"
            ],
            "גודל במ\"ר": "range",
            "מס חדרים": "range",
            "מחיר": "1-5000000"
        }
    },
        {
            "id": 1,
            "name": "רכב",
            "specs": {
                "חברה": [
                    "אאודי",
                    "אוטוביאנקי",
                    "אולדסמוביל",
                    "אופל",
                    "ב.מ.וו",
                    "ביואיק",
                    "ג'יאו - Geo",
                    "דודג'",
                    "דייהו",
                    "דייהטסו",
                    "הונדה",
                    "וולוו",
                    "טויוטה",
                    "יגואר",
                    "יונדאי",
                    "לאדה",
                    "לנציה",
                    "מאזדה",
                    "מיצובישי",
                    "מרצדס",
                    "ניסאן",
                    "סאאב",
                    "סובארו",
                    "סוזוקי",
                    "סיאט",
                    "סיטרואן",
                    "סקודה",
                    "סמארט",
                    "פיג'ו",
                    "פולקסווגן",
                    "פונטיאק",
                    "פורד",
                    "פורשה",
                    "פיאט",
                    "קאדילק",
                    "קיה",
                    "קרייזלר",
                    "רובר",
                    "רנו",
                    "שברולט",
                    "לינקולן",
                    "לקסוס",
                    "מיני",
                    "אינפיניטי",
                    "אם. ג'י. / MG",
                    "מזראטי",
                    "פרארי",
                    "אברת'",
                    "גרייט וול",
                    "אסטון מרטין",
                    "דאצ'יה",
                    "אל.טי.איי"
                ],
                "ק\"מ": "range",
                "שנה": "range",
                "יד": "range",
                "נפח מנוע": "range",
                "מחיר": "range"
            }
        },
        {
            "id": 2,
            "name": "סלולר",
            "specs": {
                "חברה": [
                    "iPhone",
                    "Asus",
                    "Gini",
                    "Blackberry",
                    "Doogee",
                    "Google",
                    "Gsmart",
                    "HTC",
                    "Huawei",
                    "Lenovo",
                    "LG",
                    "Meizu",
                    "Motorola",
                    "Nokia",
                    "OnePlus",
                    "Samsung",
                    "TELIT",
                    "Ulefone",
                    "Sony",
                    "Xiaomi",
                    "ViewSonic",
                    "ZTE"
                ],
                "זיכרון": [
                    "8",
                    "32",
                    "64",
                    "128",
                    "256"
                ],
                "צבע": [
                    "שחור",
                    "זהב",
                    "כסף",
                    "לבן",
                    "ורוד",
                    "כחול"
                ],
                "מחיר": "range"
            }
        }
    ]
    groups = [{
                 "category_id": 1,
                 "facebook_name": "pishpeshuk.cars",
                 "id": 134704043320127,
                 "name": "פשפשוק רכב"
             },
             {

                 "category_id": 2,
                 "id": 1555004694768144,
                 "name": "פשפשוק סלולר"
             },
             {
                 "category_id": 3,
                 "facebook_name": "pishpeshuk.Nadlan",
                 "id": 303803599700653,
                 "name": "פשפשוק נדלן"
             },
             {
                 "_id": "5922cd9ac8e4f945d6c041f4",
                 "category_id": 3,
                 "id": 711814002180965,
                 "name": "דירות בתל אביב להשכרה/ מכירה  Tel-Aviv Apartments"
             },
             {
                 "category_id": 3,
                 "id":458499457501175,
                 "name": "דירות להשכרה לזוגות בתל אביב"
             },
             {
                 "category_id": 3,
                 "facebook_name": "ApartmentsTelAviv",
                 "id": 45245752193,
                 "name": "דירות להשכרה ריקות או שותפים בתל אביב"
             },
             {
                 "category_id": 3,
                 "id": 232218806803833,
                 "name": "דירות להשכרה לזוגות בבאר שבע"
             },
             {
                 "category_id": 3,
                 "id": 575016292563360,
                 "name": "דירות להשכרה בין חברים באשדוד"
             },
             {
                 "category_id": 3,
                 "id": 279135451973,
                 "name": "דירות להשכרה בבאר שבע בין חברים לפני שמתפרסמות"
             },
             {
                 "category_id": 2,
                 "id": 1126777864004649,
                 "name": "פשפשוק סלולר דרום"
             },
             {
                 "category_id": 2,
                 "id": 706819216130935,
                 "name": "פשפשוק- סלולר באר שבע והסביבה"
             },
             {
                 "category_id": 1,
                 "id": 1129949647097880,
                 "name": "פשפשוק רכב באר שבע"
             }
    ]

    db = database.get_db()

    init_categories(db, categories)
    init_groups(db, groups)
    init_posts(db)


if __name__ == '__main__':
    database = Database()
    main(database)
