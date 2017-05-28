#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_data import cellular_company
from search_data import cellular_color

data = {
    'חברה': {
        'find': cellular_company.data
    },
    'מחיר': {
        'before': ['מחיר', 'מבקש', 'מחיר:', 'מבקש:'],
        'after': ['ש"ח', 'שח', '₪'],
        'regex': [ur'[\u20aa]\d+[\,\d{3}]*'],
        'type': 'int'
    },
    'זיכרון': {
        'before': ['זיכרון', 'נפח', 'זיכרון:', 'נפח:'],
        'after': ['זיכרון', 'GB', 'gb', 'ג\'יגה', 'גיגה', 'giga'],
        'regex': [r'\d*gb', r'\d*g\s'],
        'type': 'digits'
    },
    'צבע': {
        'find': cellular_color.data

    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'value_check': [r'05\d-?\d-?\d-?\d-?\d-?\d-?\d-?\d'],
        'regex': [r'05\d-?\d-?\d-?\d-?\d-?\d-?\d-?\d'],
        'type': 'digits'
    }
}


def fix(specs):
    return specs
