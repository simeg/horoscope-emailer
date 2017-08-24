#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

from src import templater


class TestCases(unittest.TestCase):
    def test_build_header(self):
        header = templater._build_header('arbitrary')
        assert header == '<h2>arbitrary</h2>\n'

    def test_build_header_with_unicode_input(self):
        header = templater._build_header('åäö-string')
        assert header == '<h2>åäö-string</h2>\n'

    def test_build_quote(self):
        quote = {
            'link': 'http://arb-domain.com',
            'quote': 'arbitrary-quote',
            'author': 'arbitrary-author',
        }
        actual = templater._build_quote('', quote)

        expected = '<h3><a href="http://arb-domain.com">Dagens Citat</a>' \
                   '</h3><p>arbitrary-quote</p><i>- arbitrary-author</i>' \
                   '\n\n<hr/>'

        assert actual == expected

    def test_build_quote_with_unicode_input(self):
        quote = {
            'link': 'http://åäö-domain.com',
            'quote': 'åäö-quote',
            'author': 'åäö-author',
        }
        actual = templater._build_quote('', quote)

        expected = '<h3><a href="http://åäö-domain.com">Dagens Citat</a>' \
                   '</h3><p>åäö-quote</p><i>- åäö-author</i>' \
                   '\n\n<hr/>'

        assert actual == expected

    def test_build_horoscopes(self):
        horoscopes = [
            {
                'website_name': 'arbitrary-name-1',
                'website_url': 'http://arb-domain-1.com',
                'result': 'arbitrary-horoscope-1',
            },
            {
                'website_name': 'arbitrary-name-2',
                'website_url': 'http://arb-domain-2.com',
                'result': 'arbitrary-horoscope-2',
            },
        ]
        actual = templater._build_horoscopes('', horoscopes)

        expected = '<h3><a href="http://arb-domain-1.com">arbitrary-name-1' \
                   '</a></h3><p>arbitrary-horoscope-1</p><hr/><h3>' \
                   '<a href="http://arb-domain-2.com">arbitrary-name-2</a>' \
                   '</h3><p>arbitrary-horoscope-2</p>'

        assert actual == expected

    def test_build_horoscopes_with_unicode_input(self):
        horoscopes = [
            {
                'website_name': 'åäö-name-1',
                'website_url': 'http://åäö-domain-1.com',
                'result': 'åäö-horoscope-1',
            },
            {
                'website_name': 'åäö-name-2',
                'website_url': 'http://åäö-domain-2.com',
                'result': 'åäö-horoscope-2',
            },
        ]
        actual = templater._build_horoscopes('', horoscopes)

        expected = '<h3><a href="http://åäö-domain-1.com">åäö-name-1' \
                   '</a></h3><p>åäö-horoscope-1</p><hr/><h3>' \
                   '<a href="http://åäö-domain-2.com">åäö-name-2</a>' \
                   '</h3><p>åäö-horoscope-2</p>'

        assert actual == expected

    def test_build_with_horoscopes(self):
        horoscopes = [
            {
                'website_name': 'arbitrary-name-1',
                'website_url': 'http://arb-domain-1.com',
                'result': 'arbitrary-horoscope-1',
            },
            {
                'website_name': 'arbitrary-name-2',
                'website_url': 'http://arb-domain-2.com',
                'result': 'arbitrary-horoscope-2',
            },
        ]
        actual = templater.build(horoscopes, None)

        expected = '<h2>It\'s Everyday Post</h2>\n<h3>' \
                   '<a href="http://arb-domain-1.com">arbitrary-name-1</a>' \
                   '</h3><p>arbitrary-horoscope-1</p><hr/><h3>' \
                   '<a href="http://arb-domain-2.com">arbitrary-name-2</a>' \
                   '</h3><p>arbitrary-horoscope-2</p>'

        assert actual == expected
