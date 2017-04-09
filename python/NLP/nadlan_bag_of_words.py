#!/usr/bin/env python
# -*- coding: utf-8 -*-


data = {
    'כתובת': {
        'before': ['ברחוב', 'ליד', 'בשכונת', 'במיקום', 'בשכונת', 'קרוב', 'בשכונה'],
        'after': [],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'גודל במ"ר': {
        'before': ['מ"ר', 'מר ', 'מטר'],
        'after': ['מ"ר', 'מר ', 'מטרים', 'מטר'],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'מס חדרים': {
        'before': ['חדרים', 'חדרים', 'חד'],
        'after': ['חדרים'],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'מחיר': {
        'before': ['מחיר'],
        'after': ['מחיר', 'ש"ח', 'שח', '₪'],
        'inside': ['ש"ח', 'שח', '₪'],
        'res': [],
        'self_res': [ur'[\u20aa]\d+[\,\d{3}]*']
    },
    'מכירה \ השכרה': {
        'before': ['למכירה', 'להשכרה'],
        'after': ['מכירה', 'השכרה'],
        'inside': ['מכירה', 'השכרה'],
        'res': [],
        'self_res': []
    },
    'טלפון': {
        'before': [],
        # ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד']
        'after': [],
        'inside': [],
        'res': [r'\d{3}-?\d{3}-?\d{4}'],
        'self_res': [r'\d{3}-?\d{3}-?\d{4}']
    }
}
