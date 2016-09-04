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


def process(lines):
    for i, l in enumerate(lines):
        logger.debug('processing line {0}:{1}'.format(i, l))


def main():
    stdin = True

    for s in sys.argv[1:]:
        if not s.startswith('-'):
            stdin = False
            logger.info('processing file {0}'.format(s))
            with open(s, encoding='utf-8', mode="rt") as f:
                process(f.read().splitlines())

    # process standard input
    if stdin:
        logger.info('processing standard input')
        process(sys.stdin.read().splitlines())


if __name__ == "__main__":
    main()
