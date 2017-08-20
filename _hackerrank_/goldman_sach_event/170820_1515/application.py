#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True


#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import * ; redirectStdio2File()


def feeOrUpfront(n, k, x, d, p):
  pass


import sys
q = int(sys.stdin.readline().strip())
for _ in xrange(q):
  [n, k, x, d] = map(int, sys.stdin.readline().strip().split(' '))
  p = map(int, sys.stdin.readline().strip().split(' '))

  result = feeOrUpfront(n, k, x, d, p)
  print(result)


if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import *; flushOutput()
