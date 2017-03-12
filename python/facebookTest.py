#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import json
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('./config.ini')

graph = facebook.GraphAPI(access_token=config.get('facebook', 'access_token'), version='2.2')

results = graph.get_object(id='1555004694768144', fields='feed')
print(json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True))

