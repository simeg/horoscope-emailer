#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging

logger = logging.getLogger(__name__)

HEADER = 'It\'s Everyday Post'


def build(horoscopes):
    logger.info('Start building horoscopes template')
    template = _build_header(HEADER)
    template = _build_horoscopes(template, horoscopes)

    logger.info('Completed building horoscopes template')
    return template


def _build_horoscopes(template, horoscopes):
    i = 0
    size = len(horoscopes)
    for hs in horoscopes:
        template += _build_hs_line(
            hs.get('website_name'),
            hs.get('website_url'),
            hs.get('result')
        ).encode('utf-8')

        # Output a divider between every horoscope
        if i != (size - 1):
            template += '<hr/>'
        i += 1
    return template


def _build_header(header):
    return '<h2>' + header + '</h2>\n'.encode('utf-8')


def _build_hs_line(name, website, horoscope):
    return '<h3><a href="' + website + '">' + name + '</a></h3><p>' \
           + horoscope + '</p>\n'.encode('utf-8')
