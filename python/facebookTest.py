#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import pprint
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('./config.ini')

graph = facebook.GraphAPI(access_token=config.get('facebook', 'access_token'), version='2.2')

feed = graph.get_object(id='134704043320127', fields='feed')

for post in feed["feed"]["data"]:
    if "message" in post:
        print post["message"] + "\n\n*****************\n"
