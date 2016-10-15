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


class Mails:
    def __init__(self):
        import imp
        credentials = imp.load_source("credentials", "/home/peter/credentials.py")
        import imaplib
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(credentials.GMAIL_USER, credentials.GMAIL_PASS)
        self.mail.select("INBOX")

    def search(self, criteria):
        result, data = self.mail.uid('search', None, criteria)
        assert result == 'OK'
        ids = data[0]  # data is a list.
        id_list = ids.split()  # ids is a space separated string
        return id_list

    def show(self, ids):
        for id in ids:
            # result, data = self.mail.uid("fetch", id, '(RFC822.HEADER)')
            result, data = self.mail.uid("fetch", id, '(BODY[HEADER.FIELDS (DATE SUBJECT)])')
            assert result == 'OK'
            print(data)

    def delete(self, ids):
        for id in ids:
            result, data = self.mail.uid("store", id, '+FLAGS', '\\Deleted')  # delete mail
            assert result == 'OK'
        self.mail.expunge()

    def close(self):
        self.mail.close()
        self.mail.logout()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __enter__(self):
        return self


def main():
    with Mails() as mbox:
        ids = mbox.search('(HEADER FROM "verify@twitter.com" Subject "New login to Twitter from ")')
        print("mails:")
        mbox.show(ids)
        print("deleting:")
        # mbox.delete(ids)


if __name__ == "__main__":
    main()
