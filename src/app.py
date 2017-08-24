#!/usr/bin/env python

import logging

from src import config_handler as cfgh, emailer, templater
from src.modules import horoscopes as horoscopes_module, quote as quote_module

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run():
    logger.info('Initiated It\'s Everyday Post')
    config = cfgh.default_config()

    email_body = _build_email(config.get('horoscopes'))

    password = cfgh.get('PASSWORD')
    username = cfgh.get('USERNAME')
    raw_recipients = cfgh.get('RECIPIENTS')
    recipients = raw_recipients.split(',')

    emailer.send(
        password,
        username,
        config.get('email').get('sender_alias'),
        recipients,
        config.get('email').get('subject'),
        email_body,
        cfgh.is_production)

    logger.info('It\'s Everyday Post execution finished')


def _build_email(horoscopes):
    horoscopes = horoscopes_module.get(horoscopes)
    quote = quote_module.get()
    return templater.build(horoscopes=horoscopes, quote=quote)


if __name__ == '__main__':
    run()
