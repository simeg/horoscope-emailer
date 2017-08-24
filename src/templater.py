#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging

logger = logging.getLogger(__name__)

HEADER = 'It\'s Everyday Post'


def build(horoscopes, quote):
    logger.info('Start building email')
    template = _build_header(HEADER)

    if quote:
        template = _build_quote(template, quote)
    if horoscopes:
        template = _build_horoscopes(template, horoscopes)

    logger.info('Completed building email')
    return template


def _build_header(header):
    return '<h2>{}</h2>\n'.format(header)


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
            hs.get('website_name'),
            hs.get('website_url'),
            hs.get('result')
        )

        # Output a divider between every horoscope
        if i != (size - 1):
            template += '<hr/>'
        i += 1
    return template


def _build_horoscope_row(name, website, horoscope):
    return '<h3>' \
           '<a href="{}">{}</a>' \
           '</h3>' \
           '<p>{}</p>' \
        .format(website, name, horoscope)
