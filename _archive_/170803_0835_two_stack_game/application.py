#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/game-of-two-stacks
"""

#TODO Fix incorrect solution

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
from _hackerrank_.util import * ; setupPycharmDebug()


def getSum(arr, x):
  t = 0
  limit = -1
  SUM = []
  for i in xrange(len(arr)):
    t += arr[i]
    SUM.append(t)

    if t>x and limit==-1:
      limit=i-1

  return SUM, limit


def doCount(aLimit, bLimit, aSum, bSum, countMax):
  for i in xrange(0, aLimit + 1):
    count = i + 1

    for j in xrange(0, bLimit + 1):
      if aSum[i] + bSum[j] > x:
        count += j
        break
      if j == bLimit:
        count += j + 1

    if count>countMax:
      countMax=count

  return countMax


import sys

g = int(sys.stdin.readline())

for _ in xrange(g):
  n,m,x = map(int, sys.stdin.readline().split(' '))
  a = map(int, sys.stdin.readline().split(' '))
  b = map(int, sys.stdin.readline().split(' '))

  aSum,aLimit = getSum(a, x)
  bSum,bLimit = getSum(b, x)

  # print n,m,x ;  print a ; print b ; print aSum ; print bSum ; print aLimit,bLimit
  # sys.stdout.flush() #write/flush immediately ref. https://stackoverflow.com/a/230774/248616

  countMax = -sys.maxint
  countMax = doCount(aLimit, bLimit, aSum, bSum, countMax)
  countMax = doCount(bLimit, aLimit, bSum, aSum, countMax)

  print(countMax)
  flushOutput()
