#!/usr/bin/env python
# -*- coding: utf-8 -*-


data = {
    'דגם': {
        'before': ['דגם', 'מסוג'],
        'after': [],
        'inside': [],
        'res': [],
        'self_res': []
    },

    'שנה': {  # לבדוק אם ניתן להסיק על שנה לפי חיפוש בטווח בין 2000 ל2017
        'before': ['עלה לכביש', 'שנת', 'מודל'],
        'after': [],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'יד': {
        'before': ['יד', 'ידיים'],
        'after': ['ידיים'],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'מחיר': {
        'before': ['מחיר', 'מבקש'],
        'after': ['ש"ח', 'שח', '₪'],
        'inside': ['ש"ח', 'שח', '₪'],
        'res': [],
        'self_res': [ur'[\u20aa]\d+[\,\d{3}]*']
    },
    'ק"מ': {
        'before': ['קמ ', 'ק"מ', 'עשה', 'עשתה', 'ק.מ', 'קילומטראז'],
        'after': ['אלף', 'KM', 'קמ', 'ק"מ', 'קילומטר'],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'נפח מנוע': {
        'before': ['מנוע'],
        'after': [],
        'inside': [],
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
