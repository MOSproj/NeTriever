#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import find_word_index, to_unicode
import re


def analyse(text, bag_of_words):
    specs = dict()
    split_message = text.split()
    for key, value in bag_of_words.items():
        spec_val = extract_word_indicator(split_message, value['before'], value['res'], 'before')
        if spec_val is not None:
            specs[key] = spec_val
        spec_val = extract_word_indicator(split_message, value['after'], value['res'], 'after')
        if spec_val is not None:
            specs[key] = spec_val
        for self_re in value['self_res']:
            results = re.findall(self_re, text)
            if len(results) > 0:
                specs[key] = results[0]
                break
    return specs


def extract_word_indicator(split_message, indicators_to_extract, res, state):
    for indicator in indicators_to_extract:
        index = find_word_index(split_message, indicator)
        for re in res:
            pass
        if index is not None:
            if state == 'before' and index + 1 < len(split_message):
                return split_message[index + 1]
            elif state == 'after' and index - 1 >= 0:
                return split_message[index - 1]
    return None
