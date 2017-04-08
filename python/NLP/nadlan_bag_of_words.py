#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {
    'ק"מ': {
        'before': [],
        'after': ['אלף'],
        'in': [],
        'regular_expression': []
    },
    'כתובת': {
        'before': ['ברחוב', 'למכירה ', 'ליד', 'בשכונת', 'במיקום', 'קרוב'],
        'after': [],
        'in': [],
        'regular_expression': []
    },
    'גודל במ"ר': {
        'before': [],
        'after': ['מ"ר', 'מר ', 'מטרים', 'מטר'],
        'in': [],
        'regular_expression': []
    },
    'מס חדרים': {
        'before': [],
        'after': ['חדרים ', 'דירת'],
        'in': [],
        'regular_expression': []
    },
    'מחיר': {
        'before': [],
        'after': ['מחיר', 'ש"ח', 'שח', '₪'],
        'in': ['ש"ח', 'שח', '₪'],
        'regular_expression': []
    },
    'מכירה \ השכרה': {
        'before': [],
        'after': [],
        'in': ['מכירה', 'השכרה'],
        'regular_expression': []
    },
    'טלפון': {
        'before': [],
        'after': ['פרטים', 'לפרטים', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'in': [],
        'regular_expression': []
    }
}