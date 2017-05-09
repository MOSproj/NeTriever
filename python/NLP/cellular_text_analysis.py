#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_data import cellular_company
from search_data import cellular_color

data = {
    'חברה': {
        'find': cellular_company.data
    },

    'מחיר': {
        'before': ['מחיר', 'מבקש'],
        'after': ['ש"ח', 'שח', '₪'],
        'regex': [ur'[\u20aa]\d+[\,\d{3}]*'],
        'type': 'int'
    },
    'זיכרון': {
        'before': ['זיכרון', 'נפח'],
        'after': ['זיכרון', 'GB', 'gb', 'ג\'יגה', 'גיגה'],
        'type': 'digits'
    },
    'צבע': {
        'find': cellular_color.data

    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'value_check': [r'\d{3}-?\d{3}-?\d{4}'],
        'regex': [r'\d{3}-?\d{3}-?\d{4}'],
        'type': 'digits'
    }
}