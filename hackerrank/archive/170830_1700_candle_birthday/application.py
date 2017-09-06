#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/birthday-cake-candles?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()

import sys
n = int(sys.stdin.readline().strip())
a = map(int, sys.stdin.readline().strip().split(' '))


def birthdayCakeCandles(n, a):
  count=0
  maxCandle = -sys.maxint

  for i in xrange(len(a)):
    if a[i]>maxCandle:
      count=1
      maxCandle = a[i]
    elif a[i]==maxCandle:
      count+=1

  return count


result = birthdayCakeCandles(n, a)
print(result)

if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()
