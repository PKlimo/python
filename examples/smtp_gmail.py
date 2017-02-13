#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import logging
log_format = '%(levelname)s:%(name)s:%(funcName)s:%(message)s'
if "-vv" in sys.argv[1:]:
    logging.basicConfig(format=log_format, level=logging.DEBUG)
elif "-v" in sys.argv[1:]:
    logging.basicConfig(format=log_format, level=logging.INFO)
else:
    logging.basicConfig(format=log_format, level=logging.WARNING)
logger = logging.getLogger(__name__)


def send_email(body):
    import smtplib
    from email.mime.text import MIMEText
    sender = 'sender@gmail.com'
    receiver = ['pklimo@gmail.com']

    msg = MIMEText(body)
    msg['Subject'] = 'subject of the mail'
    msg['From'] = sender
    msg['To'] = ", ".join(receiver)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    import imp
    credentials = imp.load_source("credentials", "/home/peter/credentials.py")
    server.login(credentials.GMAIL_USER, credentials.GMAIL_PASS)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


def main():
    send_email('body of the mail')


if __name__ == "__main__":
    main()
