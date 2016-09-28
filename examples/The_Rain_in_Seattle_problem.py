#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" You're about to get on a plane to Seattle. You want to know if you should bring an umbrella. You call 3 random friends of
yours who live there and ask each independently if it's raining. Each of your friends has a 2/3 chance of telling you the truth
and a 1/3 chance of messing with you by lying. All 3 friends tell you that "Yes" it is raining. What is the probability that it's
actually raining in Seattle?
https://www.glassdoor.com/Interview/You-re-about-to-get-on-a-plane-to-Seattle-You-want-to-know-if-you-should-bring-an-umbrella-
You-call-3-random-friends-of-y-QTN_519262.htm
http://allendowney.blogspot.sk/2016/09/bayess-theorem-is-not-optional.html
"""
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

import numpy.random


def personSay(n, rain):
    # person choose to tell true / lie (p1tf) and answer question (p1a)
    p1tf = 2 * numpy.random.binomial(1, 2.0 / 3.0, n) - 1  # -1 tell lie, 1 tell true
    p1a = rain * p1tf
    logger.debug('rain:\t\t\t{}'.format(rain[:show]))
    logger.debug('person 1 True / False:\t{}'.format(p1tf[:show]))
    logger.debug('person 1 tell rain:\t{}'.format(p1a[:show]))
    logger.debug('Generated true/false ration: {}'.format(sum(p1tf)))
    logger.debug('Expected true/false ration: {}'.format(n//3))
    error = abs(sum(p1tf)-(n//3)) / n
    logger.info('Error for true/false ration: {}'.format(error))

    logger.debug(' ')
    return p1a


def genRain(n):
    rain = 2 * numpy.random.binomial(1, 0.1, n) - 1        # -1 not raining, 1 is raining
    logger.debug('Generated rain ration: {}'.format(sum(rain)))
    logger.debug('Expected rain ration: {}'.format(8*n//10))
    error = abs(sum(rain)+(8*n//10)) / n
    logger.info('Error for rain ration: {}'.format(error))
    return rain


def simulation(n):
    logger.info('number of tries:{}'.format(n))
    rain = genRain(n)

    p1a = personSay(n, rain)
    p2a = personSay(n, rain)
    p3a = personSay(n, rain)

    # all three answers:
    paa = p1a + p2a + p3a
    logger.debug('rain:\t\t\t{}'.format(rain[:show]))
    logger.debug('All person tell rain:\t{}'.format(paa[:show]))
    logger.debug(' ')
    pos, neg = 0, 0
    for i, e in enumerate(paa):
        if e == 3:
            if rain[i] == 1:
                pos += 1
            elif rain[i] == -1:
                neg += 1
            else:
                logger.error("paa[i] is not 1 or -1, value of paa[{}]:{}".format(i, e))
    logger.debug('pos: {}, neg: {}'.format(pos, neg))
    ret = pos/(pos+neg)
    logger.info('probability, taht is raining, where all 3 persons say it is: {}'.format(ret))
    return ret


def compute():
    def P(s):
        if s == 'raining':
            return 0.1
        elif s == 'not-raining':
            return 1 - P('raining')
        elif s == 'Yes,Yes,Yes | raining':
            return (2.0 / 3.0) ** 3
        elif s == 'Yes,Yes,Yes | not-raining':
            return (1.0 / 3.0) ** 3
        elif s == 'Yes, Yes, Yes':
            return P('raining') * P('Yes,Yes,Yes | raining') + P('not-raining') * P('Yes,Yes,Yes | not-raining')
        else:
            logger.error("Error in function P() unknown argument:'{}'".format(s))

    # P('raining | Yes,Yes,Yes') = X
    X = P('raining') * P('Yes,Yes,Yes | raining') / P('Yes, Yes, Yes')
    logger.debug("p = 8/17 = {}".format(8.0 / 17.0))
    logger.info("analytic computation: {}".format(X))
    return X


if __name__ == "__main__":
    show = 20
    s1 = simulation(100000)
    print("simulation for 10**5: {}".format(s1))
    s2 = simulation(1000000)
    print("simulation for 10**6: {}".format(s2))
    c = compute()
    print("analytical computation: {}".format(c))
