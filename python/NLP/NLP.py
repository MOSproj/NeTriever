#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

    def __init__(self, category):
        pass

    @staticmethod
    def get_specs_from_post(message, category):
        return BagOfWordsAnalysis.analyse(message, NLP.bag_of_words_files[category])
