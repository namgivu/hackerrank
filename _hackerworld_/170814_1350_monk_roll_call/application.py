#!/usr/bin/env python2.7

"""
https://www.hackerearth.com/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import * ; redirectStdio2File()

import sys
N = int(sys.stdin.readline().strip())
colleagues = dict()
for _ in xrange(N):
  line = sys.stdin.readline().strip().split(' ')
  rollNum = line[0]
  colleagueName = line[1]
  colleagues[rollNum] = colleagueName

# print(colleagues)

q = int(sys.stdin.readline().strip())
for __ in xrange(q):
  r = sys.stdin.readline().strip()
  print(colleagues[r])

if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import *; flushOutput()

