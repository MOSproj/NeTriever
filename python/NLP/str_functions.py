# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re


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
