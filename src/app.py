#!/usr/bin/env python

import emailer
import requester
import templater
import config_handler as cfgh


def run():
    config = cfgh.get_default_config()

    horoscopes = requester.get_horoscopes(config.get('horoscopes'))
    html_email = templater.build(horoscopes)

    password = cfgh.get_prod_variable_else_dev('PASSWORD')
    username = cfgh.get_prod_variable_else_dev('USERNAME')
    raw_recipients = cfgh.get_prod_variable_else_dev('RECIPIENTS')
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
