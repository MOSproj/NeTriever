#!/usr/bin/env python
# -*- coding: utf-8 -*-
from FacebookPost import FacebookPost
from datetime import datetime


class DatabasePost:

    def __init__(self, post):
        if isinstance(post, dict):
            if 'ignore' in post:
                self.post = post
            else:
                self.post = self.convert_to_dict(post)
        elif isinstance(post, DatabasePost):
            self.post = post.post
        elif isinstance(post, FacebookPost):
            self.post = self.convert_to_dict(post)
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
            raise Exception('post is ignore and dosen\'t have group_id')

    def get_from_name(self):
        if not self.is_ignored():
            return self.post['from']['name']
        else:
            raise Exception('post is ignore and dosen\'t have from_name')

    def get_from_id(self):
        if not self.is_ignored():
            return self.post['from']['id']
        else:
            raise Exception('post is ignore and dosen\'t have from_id')

    def get_created_time(self):
        if not self.is_ignored():
            return self.post['created_time']
        else:
            raise Exception('post is ignore and dosen\'t have created_time')

    def get_updated_time(self):
        if not self.is_ignored():
            return self.post['updated_time']
        else:
            raise Exception('post is ignore and dosen\'t have updated_time')

    def get_last_updated(self):
        return self.post['last_updated']

    def get_message(self):
        if not self.is_ignored():
            if 'message' in self.post:
                return self.post['message']
            else:
                raise Exception('There id no message.')
        else:
            raise Exception('post is ignore and dosen\'t have message')

    def get_images(self):
        if not self.is_ignored():
            if 'image' in self.post:
                return self.post['image']
            else:
                raise Exception('There is no images.')
        else:
            raise Exception('post is ignore and dosen\'t have images')

    def is_ignored(self):
        return self.post['ignore']

    def set_phone(self, number):
        self.post['phone'] = number

    def set_price(self, price):
        self.post['price'] = price

    def set_ignore(self):
        self.post = {
            'id': self.post['id'],
            'ignore': True
        }

    def set_specs(self, specs):
        self.post['specs'] = specs

    @staticmethod
    def convert_to_dict(facebook_post):
        if isinstance(facebook_post, dict):
            facebook_post = FacebookPost(facebook_post)
        if not isinstance(facebook_post, FacebookPost):
            raise Exception('Unsupported parameter type.')

        if facebook_post.should_be_ignore():
            return {
                'id': facebook_post.get_id(),
                'ignore': True
            }

        answer = {
            'id': facebook_post.get_id(),
            'group_id': facebook_post.get_group_id(),
            'from': {
                'name': facebook_post.get_from_name(),
                'id': facebook_post.get_from_id()
            },
            'created_time': facebook_post.get_created_time(),
            'updated_time': facebook_post.get_updated_time(),
            'last_updated': datetime.utcnow(),
            'ignore': False
        }
        try:
            answer['message'] = facebook_post.get_message()
        except Exception, e:
            print e
            pass
        try:
            answer['title'] = facebook_post.get_title()
        except Exception, e:
            print e
            pass
        try:
            answer['location'] = facebook_post.get_location()
        except Exception, e:
            print e
            pass
        try:
            answer['images'] = facebook_post.get_images()
        except Exception, e:
            print e
            pass
        # TODO: insert NLP here maybe..?
        return answer

    @staticmethod
    def convert_to_database_post(post):
        return DatabasePost(DatabasePost.convert_to_dict(post))
