#!/usr/bin/env python
# -*- coding: utf-8 -*-
import specs_to_find_cellular as specs_data


class CellularCategoryNLP:

    specs = specs_data.data

    def __init__(self):
        pass

    @staticmethod
    def process_message(message):
        specs = dict()
        split_message = message.split()
        for key, value in CellularCategoryNLP.specs['words_after_indicator'].items():
            spec_by_value = CellularCategoryNLP.__extract_word_after_indicator(split_message, value)
            if spec_by_value is not None:
                specs[key] = spec_by_value
        for key, value in CellularCategoryNLP.specs['words_before_indicator'].items():
            spec_by_value = CellularCategoryNLP.__extract_word_before_indicator(split_message, value)
            if spec_by_value is not None:
                specs[key] = spec_by_value
        return specs

    @staticmethod
    def __extract_word_after_indicator(split_message, indicators_to_extract):
        index = 0
        match = False
        for word in split_message:
            for indicator in indicators_to_extract:
                if word == indicator:
                    match = True
                    break
            if not match:
                index += 1
            else:
                break
        if index != len(split_message):
            return split_message[index + 1]

    @staticmethod
    def __extract_word_before_indicator(split_message, indicators_to_extract):
        index = 0
        match = False
        for word in split_message:
            for indicator in indicators_to_extract:
                if word == indicator:
                    match = True
                    break
            if not match:
                index += 1
            else:
                break
        if index != len(split_message):
            return split_message[index - 1]


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
