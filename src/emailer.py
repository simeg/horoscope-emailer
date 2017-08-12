#!/usr/bin/env python

import yagmail


def send(password, username, sender_alias, recipients, subject, content):
    print 'Will send e-mail to ' + str(recipients)
    yag = yagmail.SMTP({username: sender_alias}, password)
    send_result = yag.send(recipients, subject, content)

    if send_result == False:
        print 'Was unable to send email, not sure why'
    else:
        print 'Email successfully sent'
