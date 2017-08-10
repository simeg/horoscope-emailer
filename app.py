#!/usr/bin/env python

import emailer
import requester
import templater

horoscopes = requester.get_horoscopes()
html_email = templater.build(horoscopes)

emailer.send('Dagens Horoskop', html_email)
