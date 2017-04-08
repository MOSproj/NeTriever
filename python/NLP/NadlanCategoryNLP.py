#!/usr/bin/env python
# -*- coding: utf-8 -*-
import specs_to_find_nadlan as specs_data


class NadlanCategoryNLP:

    specs = specs_data.data

    def __init__(self):
        pass

    @staticmethod
    def process_message(message):
        specs = dict()
        split_message = message.split()
        for key, value in NadlanCategoryNLP.specs['words_after_indicator'].items():
            spec_by_value = NadlanCategoryNLP.__extract_word_indicator(split_message, value, "after")
            if spec_by_value is not None:
                specs[key] = spec_by_value
        for key, value in NadlanCategoryNLP.specs['words_before_indicator'].items():
            spec_by_value = NadlanCategoryNLP.__extract_word_indicator(split_message, value, "before")
            if spec_by_value is not None:
                specs[key] = spec_by_value
        return specs

    @staticmethod
    def __extract_word_indicator(split_message, indicators_to_extract, state):
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
        if state == "after":
            if index != len(split_message):
                return split_message[index + 1]
        else:
            if index != len(split_message):
                return split_message[index - 1]


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
