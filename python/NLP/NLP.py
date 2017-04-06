#!/usr/bin/env python
# -*- coding: utf-8 -*-
from CarCategoryNLP import CarCategoryNLP
from CellularCategoryNLP import CellularCategoryNLP
from NadlanCategoryNLP import NadlanCategoryNLP


class NLP:

    def __init__(self, category):
        pass

    @staticmethod
    def get_specs_from_post(message, category):
        if category == u'רכב':
            category_nlp = CarCategoryNLP
        elif category == u'נדלן':
            category_nlp = NadlanCategoryNLP
        elif category == u'סלולר':
            category_nlp = CellularCategoryNLP
        else:
            raise Exception('category name error')

        return category_nlp.process_message(message)
