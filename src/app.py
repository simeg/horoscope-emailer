#!/usr/bin/env python

import config
import emailer
import requester
import templater


def run():
    horoscopes = requester.get_horoscopes(config.horoscopes)

    html_email = templater.build(horoscopes)

    emailer.send(
        config.auth.get('password'),
        config.auth.get('username'),
        config.email.get('sender_alias'),
        config.email.get('recipients'),
        config.email.get('subject'),
        html_email)

    print 'Application execution finished'

if __name__ == '__main__':
    run()
