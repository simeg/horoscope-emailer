#!/usr/bin/env python

auth = {
    'username': '',
    'password': '',
}

email = {
    'subject': 'Dagens Horoskop',
    'recipients': [''],
    'sender_alias': 'Dina Dagliga Horoskop',
}

horoscopes = [
    {
        'website_name': 'Twice',
        'website_url': 'http://www.dagenshoroskop.nu/horoskop/dagens/11/',
        'text_xpath': '(//p)[2]',
    },
]
