#!/usr/bin/env python
# -*- coding: UTF-8 -*-

HEADER = 'Dagens horoskop för stjärntecknet Vattumanen'


def build(horoscopes):
    i = 0
    size = len(horoscopes)
    template = _format_header(HEADER)
    for h in horoscopes:
        template += _format_line(h.website_name, h.website_url, h.result).encode('utf-8')
        if i != (size - 1):
            template += '<hr/>'
        i += 1

    return template


def _format_header(header):
    return '<h2>' + header + '</h2>\n'.encode('utf-8')


def _format_line(name, website, horoscope):
    return '<h3><a href="' + website + '">' + name + '</a></h3><p>' + horoscope + '</p>\n' \
        .encode('utf-8')
