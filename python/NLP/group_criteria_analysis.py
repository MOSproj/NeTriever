#!/usr/bin/env python
# -*- coding: utf-8 -*-
from str_functions import *
import re


def analyse(text, bag_of_words):
    specs = dict()
    text = prepare_text_to_analyse(text)
    split_message = text.split()

    for key, value in bag_of_words.items():
        spec_val = None
        if 'type' in value:
            value_type = value['type']
        else:
            value_type = None
        if spec_val is None and 'regex' in value:
            spec_val = extract_word_regex(text, value['regex'], value_type)
        if spec_val is None and 'before' in value:
            spec_val = extract_word_indicator(split_message, value['before'], 'before', value_type)
        if spec_val is None and 'after' in value:
            spec_val = extract_word_indicator(split_message, value['after'], 'after', value_type)
        if spec_val is None and 'find' in value:
            spec_val = extract_word_find(text, value['find'])
        if spec_val is not None:
            specs[key] = spec_val

    return specs


def extract_word_find(text, indicators):
    for key, value in indicators.items():
        for val in value:
            if to_unicode(val) in to_unicode(text):
                return key
    return None


def extract_word_regex(text, regexs, value_type):
    for regex in regexs:
        results = re.findall(regex, text)
        if len(results) > 0:
            answer = results[0]
            if value_type is not None:
                if value_type == 'int':
                    answer = to_int(answer)
                elif value_type == 'digits':
                    answer = to_digits(answer)
                elif value_type == 'float':
                    answer = to_float(answer)
            return answer
    return None


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

            if answer is not None and value_type is not None:
                if value_type == 'int':
                    answer = to_int(answer)
                elif value_type == 'digits':
                    answer = to_digits(answer)
                elif value_type == 'float':
                    answer = to_float(answer)

            if answer is not None:
                return answer

            index += 1
    return None


def prepare_text_to_analyse(text):
    text = text.replace(u', ', u' ').replace(u'. ', u' ').replace(u':', u': ').replace(u'; ', u' ').replace(u'״', u'') \
        .replace(u'"', u'').lower()
    text = remove_emojis(text)
    return text
