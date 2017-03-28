#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Main import Main


def main():
    main = Main()
    groups = main.db.get_groups()
    for group in groups:
        feed = main.facebook.get_feed(group['id'])
        new_posts, updated_posts = main.filter_posts(feed)
        data_new_posts = []
        for post in new_posts:
            data_new_posts.append(main.get_data_from_post(post))
        main.db.insert_post(data_new_posts)
        for post in updated_posts:
            post_data = main.get_data_from_post(post)
            main.db.update_post(post_data, True)


if __name__ == '__main__':
    while True:
        main()
