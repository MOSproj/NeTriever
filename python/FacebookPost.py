#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime


class FacebookPost:

    facebook_strptime = '%Y-%m-%dT%H:%M:%S+%f'

    def __init__(self, post):
        if post is FacebookPost:
            self.post = post.post
        elif post is dict:
            self.post = post
        else:
            raise Exception('Unsupported parameter type.')

    def get_post(self):
        return self.post

    def get_id(self):
        return long(self.post['id'].split('_')[1])

    def get_group_id(self):
        return long(self.post['id'].split('_')[0])

    def get_from_name(self):
        return self.post['from']['name']

    def get_from_id(self):
        return long(self.post['from']['id'])

    def get_created_time(self):
        return datetime.strptime(self.post['created_time'], FacebookPost.facebook_strptime)

    def get_updated_time(self):
        return datetime.strptime(self.post['updated_time'], FacebookPost.facebook_strptime)

    def get_message(self):
        if 'message' in self.post:
            return self.post['message']
        else:
            raise Exception('There is no message.')

    def get_images(self):
        if 'attachments' in self.post:
            answer = []
            data_at_place_0 = self.post['attachments']['data'][0]
            if 'media' in data_at_place_0:
                answer.append(data_at_place_0['media']['image'])
            elif 'subattachments' in data_at_place_0:
                for data in data_at_place_0['subattachments']['data']:
                    answer.append(data['media']['image'])
            return answer
        else:
            raise Exception('There is no images.')

    def is_ignored(self):
        return self.post['is_expired'] or self.post['is_hidden'] or not 'message' in self.post
