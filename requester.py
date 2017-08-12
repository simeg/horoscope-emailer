#!/usr/bin/env python

from lxml import html
import requests
import config

from Horoscope import Horoscope


def get_horoscopes():
    # Get config where are the websites + xpaths are stored
    paths = config.horoscopes

    result = []
    for hs in paths:
        try:
            result.append(_set_horoscope_result(hs))
        except LookupError:
            pass

    if len(result) == 0:
        raise LookupError

    return result


def _set_horoscope_result(hs):
    page = requests.get(hs.get('website_url'))
    tree = html.fromstring(page.content)
    # Let's see if this "generic" way works with all websites
    result = tree.xpath(hs.get('xpath'))[0].text.strip()

    if len(result) == 0:
        raise LookupError

    return Horoscope(hs.get('website_name'), hs.get('website_url'), result)
