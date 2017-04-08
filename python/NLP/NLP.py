#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import find_word_index, to_unicode
from BagOfWordsAnalysis import BagOfWordsAnalysis
from car_bag_of_words import data as car_bag_of_words
from cellular_bag_of_words import data as cellular_bag_of_words
from nadlan_bag_of_words import data as nadlan_bag_of_words


class NLP:

    bag_of_words_files = {
        u'רכב': car_bag_of_words,
        u'סלולר': cellular_bag_of_words,
        u'נדלן': nadlan_bag_of_words
    }

    def __init__(self):
        pass

    @staticmethod
    def analyse_database_post(database_post, category):
        if NLP.is_finding_post(database_post):
            database_post.set_ignore()
        else:
            specs = NLP.get_specs_from_post(database_post, category)
            if 'טלפון' in specs:
                database_post.set_phone(specs['טלפון'])
                del specs['טלפון']
            if 'מחיר' in specs:
                database_post.set_price(specs['מחיר'])
                del specs['מחיר']
            database_post.set_specs(specs)

    @staticmethod
    def get_specs_from_post(database_post, category):
        message = database_post.get_message()
        return BagOfWordsAnalysis.analyse(message, NLP.bag_of_words_files[category])

    @staticmethod
    def is_finding_post(post):
        words = ['מחפש', 'מחפשת', 'מחפשים', 'להחליף', 'החלפה', 'מתעניין', 'מתעניינת', 'מעוניין', 'מעוניינת']
        split_message = post.get_message().split()
        return find_word_index(split_message, words) is not None
