#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import to_unicode


class BagOfWordsAnalysis:

    def __init__(self):
        pass

    @staticmethod
    def analyse(text, bag_of_words):
        specs = dict()
        split_message = text.split()
        for key, value in bag_of_words.items():
            spec_val = BagOfWordsAnalysis.__extract_word_indicator(split_message, value['before'], 'before')
            if spec_val is not None:
                specs[key] = spec_val
            spec_val = BagOfWordsAnalysis.__extract_word_indicator(split_message, value['after'], 'after')
            if spec_val is not None:
                specs[key] = spec_val
        return specs

    @staticmethod
    def __extract_word_indicator(split_message, indicators_to_extract, state):
        index = 0
        match = False
        for word in split_message:
            for indicator in indicators_to_extract:
                if to_unicode(word) == to_unicode(indicator):
                    match = True
                    break
            if match:
                break
            else:
                index += 1
        if match:
            if state == 'after' and index != len(split_message):
                return split_message[index + 1]
            elif state == 'before' and index != len(split_message):
                return split_message[index - 1]
        else:
            return None
