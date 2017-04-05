#!/usr/bin/env python
# -*- coding: utf-8 -*-
from CarCategoryNLP import CarCategoryNLP
from CellularCategoryNLP import CellularCategoryNLP
from NadlanCategoryNLP import NadlanCategoryNLP

class Nlp:

     def nove_to_category(self ,category):

     if category == 'רכב':
          CarCategoryNLP.process_message_Car(message, 'רכב')

     elif category == 'נדלן':
          CellularCategoryNLP.process_message_Nadlan(message, 'נדלן')

     elif category == 'סלולר':
          NadlanCategoryNLP.process_message_cellular(message, 'סלולר')
return