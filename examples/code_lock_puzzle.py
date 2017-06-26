#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" A safe has a code lock that unlocks if you input the correct four digits,
in any order. The lock has a keypad the the digits 0, 1, 2, ..., 9. For example
suppose the unlock code is 1000. The safe will open for any order you input
the digits: 1000, 0100, 0010, 0001. How many different unlock codes are there?
(Two unlock codes are different if they do not contain exactly the same digits.)
https://mindyourdecisions.com/blog/2017/06/25/can-you-solve-the-code-lock-puzzle-sunday-puzzle/
https://www.youtube.com/watch?v=8vkQ85kTVm4 """

from __future__ import print_function
import sys
import logging
import unittest
from collections import Counter
log_format = '%(levelname)s:%(name)s:%(funcName)s:%(message)s'
if "-vv" in sys.argv[1:]:
    logging_level = logging.DEBUG
elif "-v" in sys.argv[1:]:
    logging_level = logging.INFO
else:
    logging_level = logging.WARNING
# logging_level = logging.INFO
# logging_level = logging.DEBUG
logging.basicConfig(format=log_format, level=logging_level, stream=sys.stdout)
# sys.stderr = None
logger = logging.getLogger(__name__)
# logger.setHandler(logging.StreamHandler(sys.stdout))

class TC(unittest.TestCase):
    def test_int2list(self):
        self.assertListEqual(int2list(1000), ['0', '0', '0', '1'])
        self.assertListEqual(int2list(100), ['0', '0', '0', '1'])
        self.assertListEqual(int2list(1), ['0', '0', '0', '1'])
        self.assertListEqual(int2list(2222), ['2', '2', '2', '2'])
        self.assertListEqual(int2list(0), ['0', '0', '0', '0'])
        self.assertListEqual(int2list(222), ['0', '2', '2', '2'])
        self.assertIsNone(int2list(-1))
        self.assertIsNone(int2list(10000))
        self.assertIsNone(int2list(2.5))

def int2list(i: int) -> set:
    if not isinstance( i, int ):  # must be integer
        return None
    if i < 0 or i > 9999:  # out of limit - only 4 digits numer
        return None
    ret = sorted(list(str(i).zfill(4)))  # convert int -> string (4 digits with leading zeroes) -> list
    logger.debug("{} {}".format(i, ret))
    return ret

def set2str(s: set) -> str:
    return "".join(sorted(s))  # Counter needs hashable objest (e.g. string)

def main():
    res = []
    for i in range(10000):
        res.append(set2str(int2list(i)))
    # print(res)
    print("number of patterns:", len(Counter(res).keys()))
    print("number of codes:", sum(Counter(res).values()))

def test():
    unittest.main(argv=['test', '-v'])  # do not pass arguments

if __name__ == "__main__":
    if "-t" in sys.argv[1:] or "--test" in sys.argv[1:]:
        test()
    else:
        main()
