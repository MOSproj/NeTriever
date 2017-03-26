#!/usr/bin/env python
# -*- coding: utf-8 -*-
import database
import fb


def main():
    groups = database.get_groups()
    for group in groups:
        feed = fb.get_posts(group['id'])
        for post in feed['data']:
            post_to_insert = dict()
            if not post['is_expired'] and not post['is_hidden'] and not database.if_exists(long(post['id'].split("_")[1])):
                post_to_insert['id'] = long(post['id'].split("_")[1])
                post_to_insert['group_id'] = long(post['id'].split("_")[0])
                post_to_insert['from'] = {
                    'name': post['from']['name'],
                    'id': long(post['from']['id'])
                }
                database.insert_post(post_to_insert)


if __name__ == '__main__':
    while True:
        main()
