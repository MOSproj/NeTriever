#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cities as cities


answer = ''
for key, val in cities.data.items():
    answer += "'" + key + "': "
    answer += "["
    answer += "' " + key + "', '" + key + " ', 'ב" + key + "'"
    answer += "],\n"

print answer