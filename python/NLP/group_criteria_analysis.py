#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import find_word_index, to_unicode
import ast
import re


def analyse(text, bag_of_words):
    specs = dict()
    split_message = text.split()

    for key, value in bag_of_words.items():
        spec_val = None
        if spec_val is None and 'regex' in value:
            for regex in value['regex']:
                results = re.findall(regex, text)
                if len(results) > 0:
                    spec_val = to_int(results[0])
                    break
        if 'type' in value:
            value_type = value['type']
        else:
            value_type = None
        if spec_val is None and 'before' in value:
            spec_val = extract_word_indicator(split_message, value['before'], 'before', value_type)
        if spec_val is None and 'after' in value:
            spec_val = extract_word_indicator(split_message, value['after'], 'after', value_type)
        if spec_val is not None:
            specs[key] = spec_val

    return specs


def extract_word_indicator(split_message, indicators_to_extract, state, value_type):
    for indicator in indicators_to_extract:
        index = 0
        for word in split_message:
            answer = None
            if to_unicode(word) == to_unicode(indicator):
                if state == 'before' and index + 1 < len(split_message):
                    answer = split_message[index + 1]
                elif state == 'after' and index - 1 >= 0:
                    answer = split_message[index - 1]
            if answer is not None:
                if value_type is not None:
                    if value_type == 'int':
                        answer = to_int(answer)
                        if answer is not None:
                            return answer
                else:
                    return answer
            index += 1
    return None

def to_int(text):
    results = re.findall("\d+(?:,\d{3})*", text)
    if len(results) > 0:
        return results[0].replace(",", "")
    return None

