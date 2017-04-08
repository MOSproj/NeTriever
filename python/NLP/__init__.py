def to_unicode(word):
    if isinstance(word, str):
        return unicode(word, "utf-8")
    else:
        return word


from NLP import NLP
