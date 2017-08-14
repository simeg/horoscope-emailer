#!/usr/bin/env python

import yagmail
import logging

logger = logging.getLogger(__name__)


def send(password, username, sender_alias, recipients, subject, content):
    logger.info('Will send e-mail to ' + str(recipients))
    yag = yagmail.SMTP({username: sender_alias}, password)
    send_result = yag.send(recipients, subject, content)

    if send_result is False:
        logger.info('Was unable to send email, not sure why')
    else:
        logger.info('Email successfully sent')
