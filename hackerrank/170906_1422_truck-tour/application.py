#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()


import sys
N = int(sys.stdin.readline().strip())

l = [] #litre
d = [] #distance

for _ in xrange(N):
  [ litre, distance ] = map(int, sys.stdin.readline().strip().split(' '))
  l.append(litre)
  d.append(distance)

# print(N, l, d)

for startAt in xrange(N):
  currentLitre = 0
  found = True
  for i in xrange(N):
    j = (startAt+i) % N           #NOTE: % operator is higher-priority than + operator
    currentLitre += l[j]          #NOTE: don't j mis-understand with startAt
    canGo = currentLitre >= d[j]  #NOTE: don't j mis-understand with startAt

    # print(startAt, j, currentLitre, d[j])

    if not canGo:
      found = False
      break

    if canGo:
      currentLitre -= d[j]

  if found:
    print startAt
    break


if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()
