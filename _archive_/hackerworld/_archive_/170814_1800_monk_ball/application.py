#!/usr/bin/env python2.7

"""
https://www.hackerearth.com/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()

import sys
K = int(sys.stdin.readline().strip())
for _ in xrange(K):
  #input
  N = int(sys.stdin.readline().strip())
  a=[]
  for __ in xrange(N):
    ball = int(sys.stdin.readline().strip())
    a.append(ball)

  #count bit
  countBit=dict()
  for ball in a:
    b = bin(ball)
    n = len(b)
    for i in xrange(n):
      if b[i]=='1':
        j = n-1 - i
        if j in countBit:
          countBit[j] += 1
        else:
          countBit[j] = 1

  # print countBit

  #find max
  countMax = -sys.maxint
  iMax = -1
  for i,count in countBit.items():
    if count>countMax:
      countMax = count
      iMax = i
    elif count==countMax:
      if i<iMax:
        iMax = i

  #output
  print(iMax)

if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()

