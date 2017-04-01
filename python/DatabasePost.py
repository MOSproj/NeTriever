#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from FacebookPost import FacebookPost


class DatabasePost:

    def __init__(self, post):
        if post is DatabasePost:
            self.post = post.post
        elif post is dict:
            self.post = post
        else:
            raise Exception('Unsupported parameter type.')

    def get_post(self):
        return self.post

    def get_id(self):
        return self.post['id']

    def get_group_id(self):
        if not self.is_ignored():
            return self.post['group_id']
        else:
            raise Exception('post id ignore and don\'t have this data')

    def get_from_name(self):
        if not self.is_ignored():
            return self.post['from']['name']
        else:
            raise Exception('post id ignore and don\'t have this data')

    def get_from_id(self):
        if not self.is_ignored():
            return self.post['from']['id']
        else:
            raise Exception('post id ignore and don\'t have this data')

    def get_created_time(self):
        if not self.is_ignored():
            return self.post['created_time']
        else:
            raise Exception('post id ignore and don\'t have this data')

    def get_updated_time(self):
        if not self.is_ignored():
            return self.post['updated_time']

    def get_message(self):
        if not self.is_ignored():
            if 'message' in self.post:
                return self.post['message']
            else:
                raise Exception('There id no message.')
        else:
            raise Exception('post id ignore and don\'t have this data')

    def get_images(self):
        if not self.is_ignored():
            if 'image' in self.post:
                return self.post['image']
            else:
                raise Exception('There id no images.')
        else:
            raise Exception('post id ignore and don\'t have this data')

    def is_ignored(self):
        return self.post['ignore']

    @staticmethod
    def convert(facebook_post):
        if facebook_post is dict:
            facebook_post = FacebookPost(facebook_post)
        if facebook_post is FacebookPost:
            answer = dict({
                'id': facebook_post.get_id(),
                'group_id': facebook_post.get_group_id(),
                'from': {
                    'name': facebook_post.get_from_name(),
                    'id': facebook_post.get_from_id()
                },
                'created_time': facebook_post.get_created_time(),
                'updated_time': facebook_post.get_updated_time()
            })
            try:
                answer['message'] = facebook_post.get_message()
            except:
                pass
            try:
                answer['images'] = facebook_post.get_images()
            except:
                pass
            return answer
        else:
            raise Exception('Unsupported parameter type.')
