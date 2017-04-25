# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re


emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)


def find_word_index(str_array, word):
    try:
        return str_array.index(to_unicode(word))
    except Exception:
        return None


def to_unicode(word):
    if isinstance(word, str):
        return unicode(word, "utf-8")
    else:
        return word


def to_int(text):
    results = re.findall("\d+(?:,?-?\d{3})*", text)
    if len(results) > 0:
        return results[0].replace(",", "").replace("-", "")
    return None


def to_float(text):
    results = re.findall("\d+(?:.\d+)*", text)
    if len(results) > 0:
        return results[0].replace(",", "")
    return None


def remove_emojis(text):
    return re.sub(emoji_pattern, ' ', text)
