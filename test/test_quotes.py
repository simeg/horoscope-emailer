#!/usr/bin/env python

import pytest
import responses

from src.modules import quote as q_mod


@pytest.fixture
def _response_complete_json():
    return {'contents': {'quotes': [{
        'quote': 'Arbitrary quote',
        'author': 'Arbitrary author',
        'permalink': 'https://arbitrary.com'}]
    }}


@pytest.fixture
def _response_missing_author_json():
    return {'contents': {'quotes': [{
        'quote': 'Arbitrary quote',
        'permalink': 'https://arbitrary.com'}]
    }}


@responses.activate
def test_good_response():
    # Setup fake response
    responses.add(responses.GET,
                  'http://quotes.rest/qod.json?category=inspire',
                  json=_response_complete_json(),
                  status=200)

    # Extract data from fake response
    quote_dict = _response_complete_json().get('contents').get('quotes')[0]
    quote = quote_dict.get('quote')
    author = quote_dict.get('author')
    link = quote_dict.get('permalink')

    # Request from website, get fake response and assert on fake response data
    assert q_mod.get() == {'quote': quote, 'author': author, 'link': link}


@responses.activate
def test_bad_status_code_response():
    responses.add(responses.GET,
                  'http://quotes.rest/qod.json?category=inspire',
                  json={'irrelevant': 'irrelevant'},
                  status=400)

    assert q_mod.get() is None


@responses.activate
def test_missing_data_response():
    responses.add(responses.GET,
                  'http://quotes.rest/qod.json?category=inspire',
                  json=_response_missing_author_json(),
                  status=200)

    assert q_mod.get() is None


@responses.activate
def test_invalid_json_response():
    '''
    def test_invalid_json_response(mocker):
    Can't get this test up and running, been looking at this article but
    not sure how much valuable information is in it:
    https://medium.com/@bfortuner/python-unit-testing-with-pytest-and-mock-197499c4623c
    responses.add(responses.GET,
                  'http://quotes.rest/qod.json?category=inspire',
                  body=ValueError('does not work'),
                  status=200)

    assert q_mod.get() is None
    '''
