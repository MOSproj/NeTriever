# !/usr/bin/env python
# -*- coding: utf-8 -*-
from . import find_word_index, to_unicode
import group_criteria_analysis
from car_text_analysis import data as car_data, fix as car_fix
from cellular_text_analysis import data as cellular_data, fix as cellular_fix
from nadlan_text_analysis import data as nadlan_data, fix as nadlan_fix

min_specs = 2
text_analysis_files = {
    u'רכב': car_data,
    u'סלולר': cellular_data,
    u'נדלן': nadlan_data
}

fix_functions = {
    u'רכב': car_fix,
    u'סלולר': cellular_fix,
    u'נדלן': nadlan_fix
}


def analyse_database_post(database_post, category_name):
    if should_be_ignore(database_post):
        database_post.set_ignore()
    else:
        specs = get_specs_from_post(database_post, category_name)
        if 'טלפון' in specs:
            database_post.set_phone(specs['טלפון'])
            del specs['טלפון']
        if 'מחיר' in specs:
            database_post.set_price(specs['מחיר'])
            del specs['מחיר']
        if 'מיקום' in specs and not database_post.has_location():
            database_post.set_location(specs['מיקום'])
            del specs['מיקום']

        fix_functions[category_name](specs)

        if len(specs) >= min_specs:
            database_post.set_specs(specs)
        else:
            database_post.set_ignore()


def get_specs_from_post(database_post, category_name):
    message = database_post.get_message()
    # TODO: insert self-re as first option
    return group_criteria_analysis.analyse(message, text_analysis_files[category_name])


def should_be_ignore(post):
    words = ['מחפש', 'מחפשת', 'מחפשים', 'להחליף', 'החלפה', 'מתעניין', 'מתעניינת', 'מעוניין', 'למישהו', 'מישהו', 'מעוניינת',
             'שתפו', 'לשתף', 'להמליץ', "ספינרים", 'מגוון', '(SOLD)']
    post_message = post.get_message()
    for word in words:
        if to_unicode(word) in post_message:
            return True
    return False
