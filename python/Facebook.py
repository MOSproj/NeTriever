#!/usr/bin/env python
# -*- coding: utf-8 -*-
import facebook


class Facebook:

    def __init__(self, config):
        access_token = config.get('facebook', 'access_token')
        self.graph = facebook.GraphAPI(access_token=access_token, version='2.2')

    def get_feed(self, group_id):
        group_id = str(group_id)
        feed = self.graph.get_object(id=group_id, fields='feed{\
            id,from,message,permalink_url,updated_time,created_time,attachments{\
                media,subattachments\
            },is_expired,is_hidden\
        }')
        return feed['feed']['data']

    def get_post(self, post_id):
        post_id = str(post_id)
        post_json = self.graph.get_object(id=post_id, fields='id,from,message,permalink_url,updated_time,created_time,attachments{\
                media,subattachments\
            },is_expired,is_hidden')
        if 'error' not in post_json:
            return post_json
        else:
            raise Exception('the post are not exist')


    def print_feed(self, group_id):
        feed = self.get_feed(group_id)
        for post in feed:
            if 'message' in post:
                print post['message'] + '\n\n*****************\n'
