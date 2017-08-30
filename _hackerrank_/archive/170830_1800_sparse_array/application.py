#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/sparse-arrays?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=3-day-campaign
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import * ; redirectStdio2File()

import sys
N = int(sys.stdin.readline().strip())

d = dict()
for _ in xrange(N):
  s = sys.stdin.readline().strip()
  if s in d: d[s]+=1
  else: d[s]=1

Q = int(sys.stdin.readline().strip())
for _ in xrange(Q):
  q = sys.stdin.readline().strip()
  if q in d: print(d[q])
  else: print(0)


if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import *; flushOutput()
