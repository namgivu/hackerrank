#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/game-of-two-stacks
"""


def getSum(arr, x):
  t = 0
  limit = None
  SUM = []
  for i in xrange(len(arr)):
    t += arr[i]
    SUM.append(t)

    if t>x and limit is None:
      limit=i-1

  return SUM, limit

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
# from util import * ; setupPycharmDebug('input.txt')

import sys
g = int(sys.stdin.readline())
for _ in xrange(g):
  n,m,x = map(int, sys.stdin.readline().split(' '))
  a = map(int, sys.stdin.readline().split(' '))
  b = map(int, sys.stdin.readline().split(' '))

  aSum,aLimit = getSum(a, x)
  bSum,bLimit = getSum(b, x)

  # print n,m,x ;  print a ; print b ; print aSum ; print bSum ; print aLimit,bLimit

  countMax = -sys.maxint

  for i in xrange(0,aLimit+1):
    count = i+1
    for j in xrange(0,bLimit+1):
      if aSum[i]+bSum[j]>x:
        count += j

    if count>countMax:
      countMax=count

  print(countMax)
