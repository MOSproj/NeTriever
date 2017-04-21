#!/usr/bin/env python
# -*- coding: utf-8 -*-
import facebook


class Facebook:

    def __init__(self, access_token):
        self.graph = facebook.GraphAPI(access_token=access_token, version='2.2')

    def get_feed(self, group_id):
        group_id = str(group_id)
        feed = self.graph.get_object(id=group_id, fields='feed{\
            id,from,message,permalink_url,updated_time,created_time,attachments{\
                media,subattachments\
            },is_expired,is_hidden\
        }')
        return feed['feed']['data']

    def print_feed(self, group_id):
        feed = self.get_feed(group_id)
        for post in feed:
            if 'message' in post:
                print post['message'] + '\n\n*****************\n'
