#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def extract_word_after_indicator(words, indicator_to_extract):
    index = 0
    for word in words:
        if word == indicator_to_extract:
            break
        index += 1

    if index != len(words):
        print(words[index + 1])


words = str.split()
extract_word_after_indicator(words, 'יד')
extract_word_after_indicator(words, 'מנוע')
extract_word_after_indicator(words, 'עשה')
extract_word_after_indicator(words, 'בטלפון')

# remove a word
query = str
stopwords = ['פיאט']
querywords = query.split()

resultwords = [word for word in querywords if word not in stopwords]
result = ' '.join(resultwords)
print result