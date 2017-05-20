#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_data import car_company
from search_data import car_yad

data = {
    'חברה': {
        'find': car_company.data
    },
    'שנה': {
        'before': ['עלה לכביש', 'שנת', 'מודל'],
        'regex': [r'19[7-9]\d', r'20[0-1]\d'],
        'type': 'int'
    },
    'יד': {
        'before': ['יד', 'ידיים'],
        'after': ['ידיים'],
        'find': car_yad.data,
        'type': 'int'
    },
    'מחיר': {
        'before': ['מחיר', 'מבקש'],
        'after': ['שח', '₪'],
        'regex': [ur'[\u20aa]\d+[\,\d{3}]*'],
        'type': 'int'
    },
    'ק"מ': {
        'before': ['עשה', 'עשתה', 'קילומטראז'],
        'after': ['אלף', 'KM', 'קמ', 'קילומטר'],
        'type': 'int'
    },
    'נפח מנוע': {
        'before': ['מנוע', 'נפח'],
        'type': 'float'
    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'value_check': [r'\d{3}-?\d{3}-?\d{4}'],
        'regex': [r'\d{3}-?\d{3}-?\d{4}'],
        'type': 'digits'
    }

}
