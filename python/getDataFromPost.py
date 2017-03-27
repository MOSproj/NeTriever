#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Main import Main


def main():
    main = Main()
    groups = main.db.get_groups()
    for group in groups:
        feed = main.facebook.get_feed(group['id'])
        filtered_posts = main.filter_posts(feed)
        for post in filtered_posts:
            main.db.insert_post(main.get_data_from_post(post))


if __name__ == '__main__':
    while True:
        main()
