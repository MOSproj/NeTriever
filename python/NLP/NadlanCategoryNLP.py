#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NadlanCategoryNLP:

    def __init__(self):
        pass

    @staticmethod
    def process_message_Nadlan(message, category):
        specs = dict()
        if category == 'נדלן':
            words = message.split()

            specs['כתובת'] = (NadlanCategoryNLP.__extract_word_after_indicator(words, [u'ברחוב ', u'למכירה ', u'ליד', u'בשכונת', u'במיקום', u'קרוב']))
            specs['גודל במ"ר'] = (NadlanCategoryNLP.__extract_word_after_indicator(words, [u'מ"ר ', u'מר ', u'מטרים', u'מטר']))
            specs['מס חדרים'] = (NadlanCategoryNLP.__extract_word_after_indicator(words, [u'מ"ר ', u'מר ', u'מטרים', u'מטר']))
            specs['מחיר'] = (NadlanCategoryNLP.__extract_word_after_indicator(words, [u'חדרים ', u'דירת ']))
            specs['מכירה\השכרה'] = (NadlanCategoryNLP.__extract_word_after_indicator(words, [u'מחיר ', u'ש"ח ', u'שח', u'₪ ']))
            specs['טלפון'] = (NadlanCategoryNLP.__extract_word_after_indicator(words, [u'מכירה ', u'השכרה ']))

            return specs
        else:
            return dict()

    @staticmethod
    def __extract_word_after_indicator(words, indicator_to_extract = []):
        index = 0
        for word in words:
            if word == indicator_to_extract:
                break
            index += 1
        if index != len(words):
            return words[index + 1]


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

    NadlanCategoryNLP.process_message_Nadlan(str, 'רכב')
