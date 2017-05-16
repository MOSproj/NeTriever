#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_data import nadlan_types
from search_data import cities

data = {
    'מיקום': {
        'find': cities.data
    },
    'גודל במ"ר': {
        'after': ['מ"ר', 'מר', 'מטרים', 'מטר'],
        'type': 'int'
    },
    'סוג': {
        'find': nadlan_types.data
    },
    'מס חדרים': {
        'after': ['חדרים', 'חד\''],
        'type': 'float'
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
        'type': 'digits'
    }
}
