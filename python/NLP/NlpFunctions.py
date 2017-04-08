#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_word_index(split_message, word_to_find):
    try:
        return split_message.index(to_unicode(word_to_find))
    except Exception:
        return None


def to_unicode(word):
    if isinstance(word, str):
        return unicode(word, "utf-8")
    else:
        return word
