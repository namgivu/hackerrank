#!/usr/bin/env python2.7

"""
https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/subham-and-binary-strings/
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import * ; redirectStdio2File()

import sys
T = int(sys.stdin.readline().strip())
for _ in xrange(T):
  N = int(sys.stdin.readline().strip())
  S = sys.stdin.readline().strip()
  zeroCount=0
  for c in S:
    if c=='0': zeroCount+=1
  print zeroCount


if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import *; flushOutput()

