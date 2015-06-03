#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import time
import sys

user = 'me@myserver.tld'
pword = 'my_secret_password'
server = 'mail.myserver.tld'
fromaddr = 'from_me@myserver.tld'
toaddr = 'to_you@yourserver.tld'
subject = 'this is the subject'
mail_body = '''
This is the email body.
'''
msg = ('From: %s\r\nTo: %s\r\n' % (fromaddr, toaddr))
msg += 'Subject: %s\r\n' % (subject)
msg += 'Date: ' + time.strftime("%a, %d %b %Y %X -0300") + '\r\n\r\n'
msg += mail_body

try:
    try:
        print 'Sending message from %s to %s' % (fromaddr, toaddr)
        smtp_conn = smtplib.SMTP(server)
        smtp_conn.set_debuglevel(0)
        smtp_conn.ehlo()
        try:
            smtp_conn.login(user, pword)
            smtp_conn.sendmail(user, toaddr, msg)
        except smtplib.SMTPAuthenticationError:
            print 'Authentication error'
            sys.exit(1)
        print 'email succesfully sent from %s to %s' % (fromaddr, toaddr)
    except smtplib.SMTPException:
        print 'Error connecting'
        sys.exit(1)
    except KeyboardInterrupt:
        print 'Canceling'
        sys.exit(2)
finally:
    smtp_conn.quit()
