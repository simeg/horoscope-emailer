#!/usr/bin/env python

from lxml import html
import requests
import config

from Horoscope import Horoscope


def get_horoscopes():
    paths = config.horoscopes

    result = []
    for hs in paths:
        result.append(_set_horoscope_result(hs))

    return result


def _set_horoscope_result(hs):
    page = requests.get(hs.get('website_url'))
    tree = html.fromstring(page.content)
    result = tree.xpath(hs.get('xpath'))[0].text
    return Horoscope(hs.get('website_name'), hs.get('website_url'), result)
