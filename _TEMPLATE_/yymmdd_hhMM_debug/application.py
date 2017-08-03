#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

DEBUG = False #turn this TRUE/False to turn ON/off for PyCharm debug; MUST turn off when submitted

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if DEBUG: from util import * ; setupPycharmDebug()

import sys
N = int(sys.stdin.readline().strip())

a = []
a = map(int, sys.stdin.readline().strip().split(' '))

print(N)
if DEBUG: from util import *; flushOutput()
print(a)

