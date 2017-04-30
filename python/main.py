#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Database import Database
from InsertPosts import InsertPosts
from UpdatePosts import UpdatePosts
from DeleteIgnore import DeleteIgnore


def main():
    insert_posts_interval = 0.5 * 60
    update_posts_interval = 5 * 60
    delete_ignore_interval = 24 * 60 * 60
    threads = []

    db = Database()
    categories = db.get_categories()
    groups_by_category = {category['name']: db.get_groups_by_category_id(category['id']) for category in categories}
    for category_name, groups in groups_by_category.items():
        new_thread = InsertPosts(category_name, groups, insert_posts_interval)
        new_thread.start()
        threads.append(new_thread)

    new_thread = UpdatePosts(update_posts_interval)
    new_thread.start()
    threads.append(new_thread)

    new_thread = DeleteIgnore(delete_ignore_interval)
    new_thread.start()
    threads.append(new_thread)


if __name__ == '__main__':
    main()
