#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CellularCategoryNLP:

    def __init__(self):
        pass

    @staticmethod
    def process_message_cellular(message, category):
        specs = dict()
        if category == 'סלולר':
            words = message.split()
            specs['סוג מכשיר'] = (CellularCategoryNLP.__extract_word_after_indicator(words, [u'דגם']))
            specs['מחיר'] = (CellularCategoryNLP.__extract_word_after_indicator(words, [u'שח', u'ש"ח', u'₪ ']))
            specs['אזור'] = (CellularCategoryNLP.__extract_word_after_indicator(words, [u'נמצא ', u'איסוף', u'לקחת']))
            specs['זיכרון'] = (CellularCategoryNLP.__extract_word_after_indicator(words,[u'זיכרון ', u'GB', u'נפח']))
            specs['צבע'] = (CellularCategoryNLP.__extract_word_after_indicator(words,[u'צבע ', u'גוון']))

            return specs
        else:
            return dict()

    @staticmethod
    def __extract_word_after_indicator(words,indicator_to_extract = []):
        index = 0
        for word in words:
            if word == indicator_to_extract:
                break
            index += 1
        if index != len(words):
            return words[index + 1]


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
