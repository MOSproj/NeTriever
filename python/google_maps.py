#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


cache = dict()


def get_location(location):
    if location in cache:
        return cache[location]
    try:
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address="' + location + '"&language=iw'
                        '&key=AIzaSyDQ04MDuEewdy8fgvlMiw1JRQuBXVtOxSA')
        json_r = r.json()
        formatted_adress = json_r[u'results'][0][u'formatted_address'].split(', ')
        country = formatted_adress[-1]
        city = formatted_adress[-2]
        if country == u'ישראל':
            cache[location] = city
            return city
        else:
            cache[location] = None
            return None
    except:
        return None

if __name__ == '__main__':
    print get_location("דרום הארץ")
