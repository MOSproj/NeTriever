#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BagOfWordsAnalysis:

    def __init__(self):
        pass

    @staticmethod
    def analyse(text, bag_of_words):
        specs = dict()
        split_message = text.split()
        for key, value in bag_of_words.items():
            spec_val = BagOfWordsAnalysis.__extract_word_indicator(split_message, value['before'], value['regular_expression'], 'before')
            if spec_val is not None:
                specs[key] = spec_val
            spec_val = BagOfWordsAnalysis.__extract_word_indicator(split_message, value['after'], value['regular_expression'], 'after')
            if spec_val is not None:
                specs[key] = spec_val
        return specs

    @staticmethod
    def __extract_word_indicator(split_message, indicators_to_extract, regular_expression, state):
        for indicator in indicators_to_extract:
            index = BagOfWordsAnalysis.__find_word_index(split_message, indicator)
            for re in regular_expression:
                pass
            if index is not None:
                if state == 'before' and index + 1 < len(split_message):
                    return split_message[index + 1]
                elif state == 'after' and index - 1 >= 0:
                    return split_message[index - 1]
        return None

    @staticmethod
    def __find_word_index(split_message, word_to_find):
        try:
            return split_message.index(BagOfWordsAnalysis.to_unicode(word_to_find))
        except Exception:
            return None

    @staticmethod
    def to_unicode(word):
        if isinstance(word, str):
            return unicode(word, "utf-8")
        else:
            return word
