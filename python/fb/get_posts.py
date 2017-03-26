#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import facebook
from ConfigParser import SafeConfigParser


def get_posts(group_id):
    config = SafeConfigParser()
    config = SafeConfigParser()
    if os.path.exists('./config.ini'):
        config.read('./config.ini')
    else:
        config.read('./../config.ini')

    graph = facebook.GraphAPI(access_token=config.get('facebook', 'access_token'), version='2.2')

    group_id = str(group_id)

    feed = graph.get_object(id=group_id, fields='feed{id,from,message,link,updated_time,created_time,attachments{subattachments},is_expired,is_hidden}')

    return feed["feed"]


if __name__ == '__main__':
    print get_posts(134704043320127)
