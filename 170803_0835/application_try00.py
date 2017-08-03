#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/game-of-two-stacks
"""


def getSum(arr):
  t = 0
  SUM = []
  for i in xrange(len(arr)):
    t += arr[i]
    SUM.append(t)
  return SUM

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
# from util import * ; setupPycharmDebug('input.txt')

import sys
g = int(sys.stdin.readline())
for _ in xrange(g):
  n,m,x = map(int, sys.stdin.readline().split(' '))
  a = map(int, sys.stdin.readline().split(' '))
  b = map(int, sys.stdin.readline().split(' '))

  aSum = getSum(a)
  bSum = getSum(b)

  # print n,m,x ;  print a ; print b ; print aSum ; print bSum

  curSum=0
  i=-1 ; j=-1
  while True:
    if i+1<n:
      xi = curSum + a[i + 1]
    else:
      xi = sys.maxint

    if j+1<m:
      xj = curSum + b[j + 1]
    else:
      xj = sys.maxint

    if xi<=xj:
      curSum = xi
      i+=1
    if xj<xi:
      curSum = xj
      j+=1

    if curSum>x:
      break

  # print i,j ;  print curSum
  print i+1 + j+1 - 1
