# !/usr/bin/env python
# -*- coding: utf-8 -*-
from . import find_word_index, to_unicode
import bag_of_words_analysis
from car_bag_of_words import data as car_bag_of_words
from cellular_bag_of_words import data as cellular_bag_of_words
from nadlan_bag_of_words import data as nadlan_bag_of_words


bag_of_words_files = {
    u'רכב': car_bag_of_words,
    u'סלולר': cellular_bag_of_words,
    u'נדלן': nadlan_bag_of_words
}


def analyse_database_post(database_post, category):
    if should_be_ignore(database_post, category):
        database_post.set_ignore()
    else:
        specs = get_specs_from_post(database_post, category)
        if 'טלפון' in specs:
            database_post.set_phone(specs['טלפון'])
            del specs['טלפון']
        if 'מחיר' in specs:
            database_post.set_price(specs['מחיר'])
            del specs['מחיר']
        database_post.set_specs(specs)


def get_specs_from_post(database_post, category):
    message = database_post.get_message()
    # TODO: insert self-re as first option
    return bag_of_words_analysis.analyse(message, bag_of_words_files[category])


def should_be_ignore(post, category):
    words = ['מחפש', 'מחפשת', 'מחפשים', 'להחליף', 'החלפה', 'מתעניין', 'מתעניינת', 'מעוניין', 'מעוניינת']
    split_message = post.get_message().split()
    for word in words:
        if find_word_index(split_message, word) is not None:
            return True
    return False
