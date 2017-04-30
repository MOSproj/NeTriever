#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import requests
from bcolors import bcolors


cache = dict()


def get_location(location):
    config = SafeConfigParser()
    config.read('./config.ini')
    if location in cache:
        return cache[location]
    try:
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address="' + location + '"&language=iw'
                                                                        '&key=' + config.get('google maps', 'key'))
        json_r = r.json()
        formatted_address = json_r[u'results'][0][u'formatted_address'].split(', ')
        country = formatted_address[-1]
        city = formatted_address[-2]
        if country == u'ישראל':
            cache[location] = city
            return city
        else:
            cache[location] = location
            return location
    except Exception, e:
        print e
        return location

if __name__ == '__main__':
    print get_location("דרום הארץ")
