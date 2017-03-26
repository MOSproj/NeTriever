#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Database
import Facebook


def main():
    database = Database.Database()
    facebook = Facebook.Facebook()
    groups = database.get_groups()
    for group in groups:
        feed = facebook.get_feed(group['id'])
        for post in feed:
            post_to_insert = dict()
            if not post['is_expired'] and not post['is_hidden'] and not database.post_id_exists(long(post['id'].split("_")[1])):
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
