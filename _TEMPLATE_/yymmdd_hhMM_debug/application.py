#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
# from util import * ; setupPycharmDebug('input.txt')

import sys
N = int(sys.stdin.readline())

a = []
a = map(int, sys.stdin.readline().split(' '))

print N, a
