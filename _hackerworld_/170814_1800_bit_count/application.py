#!/usr/bin/env python2.7

"""
https://www.hackerearth.com/practice/basic-programming/bit-manipulationd/basics-of-bit-manipulation/tutorial/
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import * ; redirectStdio2File()

import sys
K = int(sys.stdin.readline().strip())
for i in xrange(K):
  N = int(sys.stdin.readline().strip())
  n = N
  count=0
  while n>0:
    r = n % 2
    n = n / 2
    if r==1: count+=1
  print count

if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import *; flushOutput()

