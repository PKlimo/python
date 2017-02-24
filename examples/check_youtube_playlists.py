#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import imp
credentials = imp.load_source("credentials", "/home/peter/credentials.py")

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
import sarge

def print_help():
    print('usage: {0} [options]'.format(sys.argv[0]))
    print('Compare content of downloaded playlist to stored files')
    print('options:')
    print("\t --print\t print on stdout content of playlist and exit (don't send email), used for updating stored files")
    print('\t -v\t\t verbose output, on stderr print info messages')
    print('\t -vv\t\t more verbose output, on stderr print debug messages')
    print('\t --help\t\t print this help message and exit')


def send_email(telo, priloha):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart

    sender = 'check_youtube_playlist@localhost'
    receiver = ['pklimo@gmail.com']

    msg = MIMEMultipart()
    msg['Subject'] = 'difference in youtube playlist'
    msg['From'] = sender
    msg['To'] = ", ".join(receiver)

    msg.attach(MIMEText(telo))
    part = MIMEApplication(priloha.encode('ascii'), Name="swing_music.diff")
    part['Content-Disposition'] = 'attachment; filename="swing_music.diff"'
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(credentials.GMAIL_USER, credentials.GMAIL_PASS)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

def download():
    tmp = sarge.get_stdout('mktemp').rstrip()  # create temporary file and remove new line from file name
    logger.debug('temp file: {}'.format(tmp))
    pl = 'PLOnNuoRw5c6XDortZHo3FOU-4luWsEZeD'
    logger.info('downloading playlist {0}: {1}'.format('swing_music', pl))
    sarge.run('youtube-dl  --get-title --no-warnings  https://www.youtube.com/playlist?list={0} > {1}'.format(pl, tmp))
    return tmp

if __name__ == "__main__":
    if "--help" in sys.argv[1:]:
        print_help()
    else:
        store_file = "/home/peter/Dropbox/youtube/swing_music"
        text_mailu = """In attachment is enclosed diff file. To apply it, press 'v', select file, press '|' and enter the following command: 'patch -p0 -i -' """
        tmp = download()
        if "--print" in sys.argv[1:]:
            sarge.run("cat " + tmp)
        else:
            diff = sarge.run('diff -uN ' + store_file + ' ' + tmp, stdout = sarge.Capture())
            if diff.returncode != 0:  # compare stored content and downloaded data
                send_email(text_mailu, diff.stdout.text)
            sarge.run('touch -a ' + store_file)  # update access time
        sarge.run("rm " + tmp)

