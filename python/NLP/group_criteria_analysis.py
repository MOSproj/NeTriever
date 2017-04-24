#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import find_word_index, to_unicode, to_int, to_float
import re


def analyse(text, bag_of_words):
    specs = dict()
    text = text.replace(', ', ' ').replace('. ', ' ').replace(': ', ' ').replace('; ', ' ').replace(u'״', '') \
        .replace(u'"', '')
    emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
        "+", flags=re.UNICODE)
    text = re.sub(emoji_pattern, ' ', text)                  # no emoji
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
        if spec_val is not None:
            specs[key] = spec_val

    return specs


def extract_word_regex(text, regexs, value_type):
    for regex in regexs:
        results = re.findall(regex, text)
        if len(results) > 0:
            if value_type is not None:
                if value_type == 'int':
                    answer = to_int(results[0])
                    if answer is not None:
                        return answer
                if value_type == 'float':
                    answer = to_float(results[0])
                    if answer is not None:
                        return answer
            else:
                return results[0]
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
            if answer is not None:
                if value_type is not None:
                    if value_type == 'int':
                        answer = to_int(answer)
                        if answer is not None:
                            return answer
                    if value_type == 'float':
                        answer = to_float(answer)
                        if answer is not None:
                            return answer
                else:
                    return answer
            index += 1
    return None
