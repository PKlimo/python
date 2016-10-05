#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A single alien lands on Earth. Every day after that, each alien on Earth undergoes a transformation, which could be any of the
four equally likely events:
(a) the alien dies,
(b) the alien does nothing,
(c) the alien replicates itself (2 aliens total),
(d) the alien replicates itself twice (3 aliens total).
With bad luck the alien race might die out quickly. But with good luck the alien race might survive indefinitely.
What is the probability the alien race eventually dies out and goes extinct?"""

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

from numpy.random import randint
from numpy import sum
from numpy import sqrt


def next_day(n):
    livedie = randint(0, 4, n)
    end = sum(livedie)
    logger.debug("beginnig of day: {}, livedie:{}, end of day:{}".format(n, livedie, end))
    return end


def run(iterations, days):
    extinct = 0
    for i in range(iterations):
        t = simulation(days)
        logger.debug("total population:{}".format(t))
        if t == 0:
            extinct += 1
    ret = float(extinct) / float(iterations)
    logger.info("extincted:{}, total:{}, percentage:{}".format(extinct, iterations, ret))
    return ret


def simulation(days):
    t = 1
    d = 1
    while True:
        if d > days:
            break
        t = next_day(t)
        if t == 0:
            break
        # if t > 50:
        #    break
        d += 1
    logger.debug("days:{}, total population:{}".format(d, t))
    return t


def compute(days):
    def p(k):
        if k is None:  # value if k convert to infinite
            return sqrt(2)-1
        elif k == 1:
            return 1.0 / 4
        else:
            return (1.0/4) + (1.0/4)*p(k-1) + (1.0/4)*p(k-1)*p(k-1) + (1.0/4)*p(k-1)*p(k-1)*p(k-1)
    return p(days)


def main():
    iterations = 10 ** 5
    for days in range(1, 10):
        sim = run(iterations, days)
        com = compute(days)
        print("days to live:{}, simulation:{}, computation:{}, error:{}%".format(days, sim, com, 100 * abs(sim-com)))


if __name__ == "__main__":
    main()
