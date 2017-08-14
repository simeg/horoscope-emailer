#!/usr/bin/env python

import emailer
import requester
import templater
import config_handler as cfgh


def run():
    config = cfgh.get_default_config()

    horoscopes = requester.get_horoscopes(config.get('horoscopes'))
    html_email = templater.build(horoscopes)

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
        html_email)

    print 'Application execution finished'


if __name__ == '__main__':
    run()
