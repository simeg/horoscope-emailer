#!/usr/bin/env python

import requests
import logging

logger = logging.getLogger(__name__)


def get():
    logger.info('Fetching quote')
    res = requests.get('http://quotes.rest/qod.json?category=inspire')

    if res.status_code == 200:
        try:
            res_json = res.json()
            quote_dict = res_json.get('contents').get('quotes')[0]

            quote = quote_dict.get('quote')
            # The API is not trimming the output as
            # it should so we have to do it here
            quote = quote.strip()
            author = quote_dict.get('author')
            link = quote_dict.get('permalink')

            if quote and author and link:
                logger.info('Completed fetching quote')
                return {
                    'quote': quote,
                    'author': author,
                    'link': link,
                }
            else:
                logger.warn(
                    'Response from Quote API is missing data, '
                    'quote=[%s] author=[%s] link=[%s] '
                    'and entire response=[%s]',
                    quote, author, link, res_json)
                return None

        except ValueError:
            logger.warn(
                'Response from Quote API is not valid JSON=[%s]', str(res))
            return None

    else:
        logger.warn(
            'Invalid response from Quote API with status code=[%d] '
            'and response=[%s]',
            res.status_code, res.json())
        return None
