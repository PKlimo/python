#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import itertools
import random
from collections import Counter

sym = 10  # number of symbols
spc = 4   # symbols per card

class Solution:
    def __init__(self):
        self.ok = []
        self.n = []
        self.rnd = [x for x in itertools.combinations(list(range(sym)),spc)]
        random.shuffle(self.rnd)
        random.shuffle(self.rnd)
        for i in self.rnd:
            self.__add(i)

    def __add(self, k):
        for i in self.ok:
            if set(i).isdisjoint(k):
                self.n.append(k)
                return
        self.ok.append(k)

    def __hist(self):
        return Counter(list(itertools.chain(*self.ok))).values()

    def __hist_full(self):
        return Counter(list(itertools.chain(*self.ok)))

    def score(self):
        return max(self.__hist())  - min(self.__hist())

    def print_header(self):
        print("number of symbols: {}".format(sym))
        print("number of used symbols: {}".format(len(self.__hist())))
        print("symbols per card:  {}".format(spc))
        print("number of cards: {}".format(len(self.ok)))
        print("number of A4 papers: {} (8 cards in one paper)".format(len(self.ok) / 8))
        print("histogram with indexes: {}".format(self.__hist_full()))
        print("histogram: {}".format(self.__hist()))
        print("hist min: {}".format(min(self.__hist()) ))
        print("hist max: {}".format(max(self.__hist()) ))
        print("hist dif: {}".format(max(self.__hist())  - min(self.__hist()) ))
        print("score: {}".format(self.score()))

    def print_solution(self):
        for i in self.ok:
            print(i)

def main():
    best = Solution()
    for _ in range(1000):
        temp = Solution()
        if best.score() > temp.score():
            best = temp
    best.print_header()
    best.print_solution()

if __name__ == "__main__":
    main()
