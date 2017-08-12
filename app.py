#!/usr/bin/env python

import emailer
import requester
import templater


def run():
    horoscopes = None
    try:
        horoscopes = requester.get_horoscopes()
    except LookupError:
        print "Aborting since there's no horoscopes to process"
        quit()

    html_email = templater.build(horoscopes)

    emailer.send('Dagens Horoskop', html_email)


if __name__ == "__main__":
    run()
