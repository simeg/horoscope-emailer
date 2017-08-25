#!/usr/bin/env python
# coding=utf-8

import logging

logger = logging.getLogger(__name__)


def build(horoscopes, quote):
    logger.info('Start building email')
    template = ''

    if quote:
        template = _build_quote(template, quote)
    if horoscopes:
        template = _build_horoscopes(template, horoscopes)

    logger.info('Completed building email')
    return template


def _build_quote(template, quote):
    return template + '<h3><a href="{}">Dagens Citat</a></h3>' \
                      '<p>{}</p>' \
                      '<i>- {}</i>' \
                      '\n\n<hr/>' \
        .format(quote.get('link'),
                quote.get('quote'),
                quote.get('author'))


def _build_horoscopes(template, horoscopes):
    i = 0
    size = len(horoscopes)
    for hs in horoscopes:
        template += _build_horoscope_row(
            hs.get('website_url'),
            hs.get('website_name'),
            hs.get('result')
        )

        # Output a divider between every horoscope
        if i != (size - 1):
            template += '<hr/>'
        i += 1
    return template


def _build_horoscope_row(url, name, horoscope):
    return '<h3>' \
           '<a href="{}">{}</a>' \
           '</h3>' \
           '<p>{}</p>' \
        .format(url, name, horoscope)
