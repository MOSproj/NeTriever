#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_data import car_company
from search_data import car_yad

data = {
    'חברה': {
        'find': car_company.data
    },
    'שנה': {
        'before': ['עלה לכביש', 'שנת', 'מודל', 'שנה:', 'מודל:'],
        'regex': [r'\D19[7-9]\d\D', r'\D20[0-1]\d\D'],
        'type': 'int'
    },
    'יד': {
        'before': ['יד', 'ידיים'],
        'after': ['ידיים'],
        'find': car_yad.data,
        'type': 'int'
    },
    'מחיר': {
        'before': ['מחיר', 'מבקש', 'מבקשת'],
        'after': ['שח', '₪'],
        'regex': [ur'[\u20aa]\d+[\,\d{3}]*'],
        'type': 'int'
    },
    'ק"מ': {
        'before': ['עשה', 'עשה:', 'עשתה', 'עשתה:', 'קילומטראז', 'קילומטראז:', 'ק"מ:', 'קמ:', 'קילומטר:'],
        'after': ['אלף', 'KM', 'קמ', 'קילומטר'],
        'type': 'int'
    },
    'נפח מנוע': {
        'before': ['מנוע', 'נפח', 'מנוע:', 'נפח:'],
        'after': ['סמ״ק'],
        'type': 'float'
    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'value_check': [r'\d{3}-?\d{3}-?\d{4}'],
        'regex': [r'\d{3}-?\d{3}-?\d{4}'],
        'type': 'digits'
    }
}


def fix(specs):
    if 'שנה' in specs:
        year = specs['שנה']
        if 70 <= year <= 99:
            specs['שנה'] = 1900 + year
        elif 01 <= year <= 19:
            specs['שנה'] = 2000 + year
    if 'ק"מ' in specs:
        km = specs['ק"מ']
        if km < 1000:
            specs['ק"מ'] = km*1000
    if 'נפח מנוע' in specs:
        ec = specs['נפח מנוע']
        if ec < 1000:
            specs['נפח מנוע'] = ec*1000
        if ec == 2000:
            if 'שנה' in specs and specs['שנה'] == 2000:
                del specs['שנה']

