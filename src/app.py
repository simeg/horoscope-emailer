#!/usr/bin/env python

import config_handler as cfgh
import emailer
import logging
import templater

from modules import horoscopes as mod_hs
from modules import quote as mod_q

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
    horoscopes = mod_hs.get(horoscopes)
    quote = mod_q.get()
    return templater.build(horoscopes=horoscopes, quote=quote)


if __name__ == '__main__':
    run()
