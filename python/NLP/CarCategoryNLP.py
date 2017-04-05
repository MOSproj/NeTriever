#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CarCategoryNLP:

    extract_after_indicator = {
        u'דגם': ['דגם', 'מסוג'],
        u'שנה': ['עלה לכביש', 'שנת', 'מודל'],
        u'יד': ['יד', 'ידיים'],
        u'מחיר': ['מחיר', 'מחיר:'],
        u'ק"מ': ['קמ ', 'ק"מ', 'אלף', 'KM', 'עשה', 'ק.מ', 'קילומטראז'],
        u'טלפון': ['פרטים', 'לפרטים', 'נייד', 'נוספים', 'פלאפון', 'בנייד']
    }

    extract_before_indicator = {
        u'ק"מ': ['אלף']
    }

    def __init__(self):
        pass

    @staticmethod
    def process_message_car(message, category):
        specs = dict()
        if category == 'רכב':
            words = message.split()
            for key, value in CarCategoryNLP.extract_after_indicator.items():
                spec_by_value = CarCategoryNLP.__extract_word_after_indicator(words, value)
                if spec_by_value is not None:
                    specs[key] = spec_by_value
            for key, value in CarCategoryNLP.extract_before_indicator.items():
                spec_by_value = CarCategoryNLP.__extract_word_before_indicator(words, value)
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
פיאט פונטו HGT 2002
מנוע 1800 138 כ״ס.
הרכב יד 4 עשה 210 אלף קילומטר
מטופל בשמנים הכי איכותיים מבית Agip.
תוספות:
קויילאוברים kw יחידים בארץ לרכב הזה ניתן לכוון גובה וקשיחות.
מוט מיצב קדמי עליון omp
צמיגי טויו R1R בני שלושה חודשים
ספייסרים omp
פנסי אנג'ל אייז עם קסנון!
אגזוז של אבארט 500 (רעש ממכר)
דאבל דין עם בנייה מיוחדת שכוללת מצלמת רוורס
מגבר עם קומפוננט מורל טמפו.
תפירת ריקמת סמלי אבארט בסלון.
הרכב עשה טיפול החודש הכולל גומיות שסתומים,טיימינג ומותחנים,שמנים, פלגים, אטם מכסה שסתומים!
הרכב מדוגם והושקע בו המון ושמור ברמה הכי פדנטית שיש.
רכב עם חווית נהיגה יוצאת דופן, קארטינג חוקי על הכביש!
לרציניים בלבד בטלפון 0506454813
*נמכר ללא ההגה שבתמונה!
'''

    print CarCategoryNLP.process_message_car(str, 'רכב')
