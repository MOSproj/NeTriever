#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {
    'שם המכשיר': {
        'before': ['דגם', 'מסוג'],
        'after': [],
        'inside': [],
        'regular_expression': []
    },
    'מחיר': {
        'before': ['מחיר', 'ש"ח', 'שח', '₪'],
        'after': ['ש"ח', 'שח', '₪'],
        'inside': [],
        'regular_expression': []
    },
    'אזור': {
        'before':  ['לקחת', 'איסוף', 'נמצא'],
        'after': [],
        'inside': [],
        'regular_expression': []
    },
    'זיכרון': {
        'before': ['זיכרון', 'GB', 'נפח'],
        'after': ['זיכרון', 'GB', 'גיגה'],
        'inside': [],
        'regular_expression': []
    },
    'צבע': {
        'before': ['צבע'],
        'after': [],
        'inside': [],
        'regular_expression': []
    },
    'טלפון': {
        'before': [],
        'after': ['פרטים', 'לפרטים', 'נייד', 'נוספים', 'פלאפון', 'בנייד'],
        'inside': [],
        'regular_expression': []
    }
}

