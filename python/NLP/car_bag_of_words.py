#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {
    'דגם': {
        'before': ['דגם', 'מסוג'],
        'after': [],
        'inside': [],
        'regular_expression': []
    },

    'שנה': {  # לבדוק אם ניתן להסיק על שנה לפי חיפוש בטווח בין 2000 ל2017
        'before': ['עלה לכביש', 'שנת', 'מודל'],
        'after': [],
        'inside': [],
        'regular_expression': []
    },
    'יד': {
        'before': ['יד', 'ידיים'],
        'after': ['ידיים'],
        'inside': [],
        'regular_expression': []
    },
    'מחיר': {
        'before': ['מחיר','מבקש'],
        'after': ['מחיר', 'ש"ח', 'שח', '₪'],
        'inside': ['ש"ח', 'שח', '₪'],
        'regular_expression': []
    },
    'ק"מ': {
        'before': ['קמ ', 'ק"מ', 'עשה', 'עשתה', 'ק.מ', 'קילומטראז'],
        'after': ['אלף', 'KM'],
        'inside': [],
        'regular_expression': []
    },
    'נפח מנוע': {
        'before': ['מנוע'],
        'after': [],
        'inside': [],
        'regular_expression': []
    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'after': [],
        'inside': [],
        'regular_expression': []
    }
}

