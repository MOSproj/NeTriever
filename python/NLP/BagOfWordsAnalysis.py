#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BagOfWordsAnalysis:

    def __init__(self):
        pass

    @staticmethod
    def analyse(text, bag_of_words):
        specs = dict()
        split_message = text.split()
        for key, value in bag_of_words['words_after_indicator'].items():
            spec = BagOfWordsAnalysis.__extract_word_indicator(split_message, value, "after")
            if spec is not None:
                specs[key] = spec
        for key, value in bag_of_words['words_before_indicator'].items():
            spec_by_value = BagOfWordsAnalysis.__extract_word_indicator(split_message, value, "before")
            if spec_by_value is not None:
                specs[key] = spec_by_value
        return specs

    @staticmethod
    def __extract_word_indicator(split_message, indicators_to_extract, state):
        index = 0
        match = False
        for word in split_message:
            for indicator in indicators_to_extract:
                if BagOfWordsAnalysis.to_unicode(word) == BagOfWordsAnalysis.to_unicode(indicator):
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

    @staticmethod
    def to_unicode(word):
        if isinstance(word, str):
            return unicode(word, "utf-8")
        else:
            return word
