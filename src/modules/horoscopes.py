#!/usr/bin/env python

from lxml import html
import requests
import logging

logger = logging.getLogger(__name__)


def get(horoscope_paths):
    logger.info('Fetching horoscopes')
    result = map(lambda hs: _create_horoscope(hs), horoscope_paths)

    if not result or None in result:
        raise NoHoroscopesFoundError

    logger.info('Completed fetching horoscopes')
    return tuple(result)


def _create_horoscope(hs):
    try:
        url = requests.get(hs.get('website_url'))
        tree = html.fromstring(url.content)
        # Let's see if this "generic" way works with all websites
        xpath = tree.xpath(hs.get('text_xpath'))

        if not xpath:
            return None

        # Always get the first one, even though
        # the horoscope might be spread out over
        # multiple elements
        # TODO: Support multiple elements
        result = xpath[0].text

        if not result:
            return None

        return {
            'website_name': hs.get('website_name'),
            'website_url': hs.get('website_url'),
            'result': result
        }

    except Exception:
        logger.info('Something went wrong when parsing the following'
                    ' horoscope=[' + str(hs) + ']')
        return None


class NoHoroscopesFoundError(Exception):
    pass
