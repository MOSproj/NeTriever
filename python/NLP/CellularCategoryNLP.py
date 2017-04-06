#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

class CellularCategoryNLP:

    def __init__(self):
        pass

    @staticmethod
    def process_message(message, category):
        specs = dict()
        if category == 'סלולר':
            words = message.split()
            for key, value in CellularCategoryNLP.extract_after_indicator.items(): # for key, value in CellularCategoryNLP.specs_to_find_car.items():
                spec_by_value = CellularCategoryNLP.__extract_word_after_indicator(words, value)
                if spec_by_value is not None:
                    specs[key] = spec_by_value
            for key, value in CellularCategoryNLP.extract_before_indicator.items():
                spec_by_value = CellularCategoryNLP.__extract_word_before_indicator(words, value)
                if spec_by_value is not None:
                    specs[key] = spec_by_value
            return specs
        else:
            return dict()

    @staticmethod
    def __extract_word_after_indicator(words, indicators_to_extract):
        index = 0
        match = False
        for word in words:
            for indicator in indicators_to_extract:
                if word == indicator:
                    match = True
                    break
            if not match:
                index += 1
            else:
                break
        if index != len(words):
            return words[index + 1]

    @staticmethod
    def __extract_word_before_indicator(words, indicators_to_extract):
        index = 0
        match = False
        for word in words:
            for indicator in indicators_to_extract:
                if word == indicator:
                    match = True
                    break
            if not match:
                index += 1
            else:
                break
        if index > 1:
            return words[index - 1]


if __name__ == '__main__':

    str = '''
Xiaomi  red mi note 3
₪ 700
קריית אתא
המכשיר בן פחות משנה. במצב חדש נמכר עקב קבלת מתנה פלאפון חדש.
 נמסר יחד עם כיסוים חדשים שרכשתי וקופסא מקורית ומטען מקורי .
 0546874216

'''

    CellularCategoryNLP.process_message_cellular(str, 'סלולר')
