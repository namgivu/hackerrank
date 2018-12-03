#!/usr/bin/env python2.7

"""
https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/tutorial/
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()


import sys
S = sys.stdin.readline().strip()

c='0'
d=dict()
for c in xrange(10):
  d[str(c)]=0

for c in S:
  d[c]+=1

for c in xrange(10):
  c = str(c)
  print('%s %s' % (c, d[c]))

if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()

