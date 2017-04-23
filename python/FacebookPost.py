#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime


class FacebookPost:

    facebook_strptime = '%Y-%m-%dT%H:%M:%S+%f'

    def __init__(self, post):
        if isinstance(post, FacebookPost):
            self.post = post.post
        elif isinstance(post, dict):
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

    def get_last_updated(self):
        return datetime.strptime(self.post['last_updated'], FacebookPost.facebook_strptime)

    def get_message(self):
        if 'message' in self.post:
            return self.post['message']
        raise Exception('There is no message.')

    def get_title(self):
        if 'message' in self.post:
            if self.is_sale_post():
                title = self.post['message'].split('\n', 1)[0]
                if 1 < len(title) < 66:
                    return title
                raise Exception('Title is too long.')
        raise Exception('There is no title.')

    def get_location(self):
        if 'message' in self.post:
            if self.is_sale_post():
                location_and_price = self.post['message'].split('\n')[1]
                return location_and_price[location_and_price.index('-')+2:]
        raise Exception('There is no location.')

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
        raise Exception('There is no images.')

    def is_sale_post(self):
        return 'sale_post_id' in self.post['permalink_url']

    def should_be_ignore(self):
        return ('is_expired' in self.post and self.post['is_expired']) or ('is_hidden' in self.post and self.post['is_hidden']) or 'message' not in self.post
