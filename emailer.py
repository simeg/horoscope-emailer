#!/usr/bin/env python

import yagmail

MY_EMAIL = ''
APP_PWD = ''
SENDER_ALIAS = 'Horoscoper'


def send(subject, content):
    yag = yagmail.SMTP({MY_EMAIL: SENDER_ALIAS}, APP_PWD)
    yag.send(MY_EMAIL, subject, content)
