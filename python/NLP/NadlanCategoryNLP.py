#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

class NadlanCategoryNLP:

    def __init__(self):
        pass

    with open('specs_to_find_nadlan') as data_file:
        self.data = json.load(data_file)



    @staticmethod
    def process_message_car(message, category):
        specs = dict()
        if category == 'נדלן':
            words = message.split()
            for key, value in NadlanCategoryNLP.extract_after_indicator.items(): # for key, value in NadlanCategoryNLP.specs_to_find_car.items():
                spec_by_value = NadlanCategoryNLP.__extract_word_after_indicator(words, value)
                if spec_by_value is not None:
                    specs[key] = spec_by_value
            for key, value in NadlanCategoryNLP.extract_before_indicator.items():
                spec_by_value = NadlanCategoryNLP.__extract_word_before_indicator(words, value)
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
להשכרה דירת 2.5 חדרים משופצת ומעוצבת עם מרפסת שמש ומעלית ליד כיכר רבין 7500 ש"ח!!!
 דירה מרווחת, סלון ענק עם ויטרינה גדולה ויציאה למרפסת שמש מפנקת,
  חדר שינה עם ארון קיר גדול ויציאה נוספת למרפסת. מטבח מפנק, חדר רחצה מרווח עם מקלחון
 ומקום למכונת כביסה ומייבש. חצי חדר נוסף שיכול לשמש כחדר לילד או כמשרד. בניין עם מעלית.
  שנת אופציה באותו מחיר, בעלי דירה מקסימים!!! יש חניון קרוב שאפשר לשכור חניה למעוניינים!!!!
מחיר: 7500 ש"ח
לתיאום 052-222-4402
 תיווך

'''

    NadlanCategoryNLP.process_message_Nadlan(str, 'נדלן')
