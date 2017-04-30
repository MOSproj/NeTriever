#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {
    'כתובת': {
        'before': ['ברחוב', 'ליד', 'בשכונת', 'במיקום', 'בשכונת', 'קרוב', 'בשכונה'],
    },
    'גודל במ"ר': {
        'before': ['מ"ר', 'מר', 'מטר'],
        'after': ['מ"ר', 'מר', 'מטרים', 'מטר'],
        'type': 'int'
    },
    'מס חדרים': {
        'before': ['חדרים', 'חדרים', 'חד'],
        'after': ['חדרים'],
        'type': 'int'
    },
    'מחיר': {
        'before': ['מחיר', 'מבקש'],
        'after': ['ש"ח', 'שח', '₪'],
        'regex': [ur'[\u20aa]\d+[\,\d{3}]*'],
        'type': 'int'
    },
    'מכירה \ השכרה': {
        'find': {
            'מכירה': ['למכירה', 'מכירה', "להשקעה", 'מוכר'],
            'השכרה': ['השכרה', 'להשכרה']
        },
    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'value_check': [r'\d{3}-?\d{3}-?\d{4}'],
        'regex': [r'\d{3}-?\d{3}-?\d{4}'],
        'type': 'int'
    }
}
