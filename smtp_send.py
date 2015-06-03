#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import time
import sys

# User editable settings
user_auth = 'me@myserver.tld'
pword = 'my_secret_password'
server = 'mail.myserver.tld'
fromaddr = 'from_me@myserver.tld' # In case it's different from user_auth
toaddr = 'to_you@yourserver.tld'
subject = 'This is the subject'

mail_body = '''
This is the email body.
'''

# Compose the message
msg = ('From: %s\r\nTo: %s\r\n' % (fromaddr, toaddr))
msg += 'Subject: %s\r\n' % (subject)
msg += 'Date: ' + time.strftime("%a, %d %b %Y %X -0300") + '\r\n\r\n'
msg += mail_body

# Try sending the mail, and catch some common errors
try:
    try:
        print 'Sending message from %s to %s' % (fromaddr, toaddr)
        smtp_conn = smtplib.SMTP(server)
        smtp_conn.set_debuglevel(0)
        smtp_conn.ehlo()
        try:
            # TODO: try other authentication methods, use SSL/TLS
            smtp_conn.login(user_auth, pword)
            smtp_conn.sendmail(user_auth, toaddr, msg)
        except smtplib.SMTPAuthenticationError:
            print 'Authentication error'
            sys.exit(1)
        print 'Message succesfully sent from %s to %s' % (fromaddr, toaddr)
    except smtplib.SMTPException:
        print 'Error connecting'
        sys.exit(1)
    except KeyboardInterrupt:
        print 'Canceling'
        sys.exit(2)
finally:
    smtp_conn.quit()
