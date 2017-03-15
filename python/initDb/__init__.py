import pymongo
from bson.dbref import DBRef


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
            print "pymongo.errors.DuplicateKeyError: " + category["name"] + "category"
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
