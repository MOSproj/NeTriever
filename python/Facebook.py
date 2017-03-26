#!/usr/bin/env python
# -*- coding: utf-8 -*-
import facebook
from ConfigParser import SafeConfigParser


class Facebook:

    def __init__(self):
        self.config = SafeConfigParser()
        self.config.read('./config.ini')
        self.graph = facebook.GraphAPI(access_token=self.config.get('facebook', 'access_token'), version='2.2')

    def get_feed(self, group_id):
        group_id = str(group_id)
        feed = self.graph.get_object(id=group_id, fields='feed{id,from,message,link,updated_time,created_time,attachments{subattachments},is_expired,is_hidden}')
        return feed['feed']['data']

    def print_feed(self, group_id):
        feed = self.get_feed(group_id)
        for post in feed:
            if "message" in post:
                print post["message"] + "\n\n*****************\n"
