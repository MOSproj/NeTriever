#!/usr/bin/env python
# -*- coding: utf-8 -*-
from search_data import cellular_company
from search_data import cellular_colur
from search_data import cellular_memory

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
    'אזור': {
        'before':  ['לקחת', 'איסוף', 'נמצא'],
    },
    'זיכרון': {
        'find': cellular_memory.data,
        'before': ['זיכרון', 'GB', 'gb', 'נפח'],
        'after': ['זיכרון', 'GB','gb', 'ג\'יגה'],
        'type': 'int'
},
    'צבע': {
        'find': cellular_colur.data

    },
    'טלפון': {
        'before': ['פרטים', 'לפרטים', 'בטלפון', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'value_check': [r'\d{3}-?\d{3}-?\d{4}'],
        'regex': [r'\d{3}-?\d{3}-?\d{4}'],
        'type': 'int'
    }
}
