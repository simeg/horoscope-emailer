#!/usr/bin/env python

import emailer
import requester
import templater

import yaml


def run():
    config = _get_config()

    horoscopes = requester.get_horoscopes(config.get('horoscopes'))
    html_email = templater.build(horoscopes)

    emailer.send(
        config.get('auth').get('password'),
        config.get('auth').get('username'),
        config.get('email').get('sender_alias'),
        config.get('email').get('recipients'),
        config.get('email').get('subject'),
        html_email)

    print 'Application execution finished'


def _get_config():
    with open('src/config.yaml', 'r') as cfg_file:
        return yaml.load(cfg_file)


if __name__ == '__main__':
    run()
