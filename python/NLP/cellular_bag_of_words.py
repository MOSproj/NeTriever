#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {
    'שם המכשיר': {
        'before': ['דגם', 'מסוג'],
        'after': [],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'מחיר': {
        'before': ['מחיר', 'ש"ח', 'שח', '₪'],
        'after': ['ש"ח', 'שח', '₪'],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'אזור': {
        'before':  ['לקחת', 'איסוף', 'נמצא'],
        'after': [],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'זיכרון': {
        'before': ['זיכרון', 'GB', 'נפח'],
        'after': ['זיכרון', 'GB', 'ג\'יגה'],
        'inside': [],
        'res': [],
        'self_res': []
    },
    'צבע': {
        'before': ['צבע'],
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

