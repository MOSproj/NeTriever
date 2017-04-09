#!/usr/bin/env python
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
