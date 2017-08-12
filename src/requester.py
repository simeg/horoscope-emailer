#!/usr/bin/env python

from lxml import html
import requests


def get_horoscopes(horoscope_paths):
    result = map(lambda hs: _create_horoscope(hs), horoscope_paths)

    if not result or None in result:
        raise NoHoroscopesFoundError

    return result


def _create_horoscope(hs):
    url = requests.get(hs.get('website_url'))
    tree = html.fromstring(url.content)
    # Let's see if this "generic" way works with all websites
    xpath = tree.xpath(hs.get('text_xpath'))

    if not xpath:
        return None

    result = xpath[0].text

    if not result:
        return None

    return {
        'website_name': hs.get('website_name'),
        'website_url': hs.get('website_url'),
        'result': result
    }


class NoHoroscopesFoundError(Exception):
    pass
