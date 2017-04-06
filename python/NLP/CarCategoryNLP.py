#!/usr/bin/env python
# -*- coding: utf-8 -*-
import specs_to_find_car as specs_data


class CarCategoryNLP:

    specs = specs_data.data

    def __init__(self):
        pass

    @staticmethod
    def process_message_car(message):
        specs = dict()
        split_message = message.split()
        for key, value in CarCategoryNLP.specs['words_after_indicator'].items():
            spec_by_value = CarCategoryNLP.__extract_word_after_indicator(split_message, value)
            if spec_by_value is not None:
                specs[key] = spec_by_value
        for key, value in CarCategoryNLP.specs['words_before_indicator'].items():
            spec_by_value = CarCategoryNLP.__extract_word_before_indicator(split_message, value)
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
        if index > 1:
            return split_message[index - 1]


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
    print CarCategoryNLP.process_message_car(str)
