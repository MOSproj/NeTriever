#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {

    'כתובת': {
        'before': ['ברחוב', 'ליד', 'בשכונת', 'במיקום', 'בשכונת', 'קרוב', 'בשכונה'],
        'after': [],
        'inside': [],
        'regular_expression': []
    },
    'גודל במ"ר': {
        'before': ['מ"ר', 'מר', 'מטר'],
        'after': ['מ"ר', 'מר', 'מטרים', 'מטר'],
        'inside': [],
        'regular_expression': []
    },
    'מס חדרים': {
        'before': ['חדרים', 'דירת'],
        'after': ['חדרים'],
        'inside': [],
        'regular_expression': []
    },
    'מחיר': {
        'before': ['מחיר'],
        'after': ['מחיר', 'ש"ח', 'שח', '₪'],
        'inside': ['ש"ח', 'שח', '₪'],
        'regular_expression': []
    },
    'מכירה \ השכרה': {
        'before': ['למכירה', 'להשכרה'],
        'after': ['מכירה', 'השכרה'],
        'inside': ['מכירה', 'השכרה'],
        'regular_expression': []
    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'after': [],
        'inside': [],
        'regular_expression': []
    }
}