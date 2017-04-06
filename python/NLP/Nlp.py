#!/usr/bin/env python
# -*- coding: utf-8 -*-
from CarCategoryNLP import CarCategoryNLP
from CellularCategoryNLP import CellularCategoryNLP
from NadlanCategoryNLP import NadlanCategoryNLP


class Nlp:

    def __init__(self, category):
        if category == 'רכב':
            self.category_nlp = CarCategoryNLP
        elif category == 'נדלן':
            self.category_nlp = NadlanCategoryNLP
        elif category == 'סלולר':
            self.category_nlp = CellularCategoryNLP

