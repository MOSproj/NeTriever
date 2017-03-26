#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
from ConfigParser import SafeConfigParser


def main():
    config = SafeConfigParser()
    config.read('./config.ini')

    graph = facebook.GraphAPI(access_token=config.get('facebook', 'access_token'), version='2.2')

    feed = graph.get_object(id='134704043320127', fields='feed{id,from,message,link,updated_time,created_time,attachments{subattachments},is_expired,is_hidden}')

    for post in feed["feed"]["data"]:
        if "message" in post:
            print post["message"] + "\n\n*****************\n"

if __name__ == '__main__':
    main()
