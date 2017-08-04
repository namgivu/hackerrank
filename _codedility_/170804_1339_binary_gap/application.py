#!/usr/bin/env python2.7

"""
https://codility.com/c/run/trainingM99BB7-WPG
"""


def solution(N):
  b = bin(N)[2:]
  # print(b)

  n = len(b)
  import sys ; countMax = -sys.maxint
  count = 0
  for i in xrange(n):
    if b[i]=='1':
      if count>countMax:
        countMax = count
      count=0

    elif b[i]=='0':
      count+=1

      #count for the trailing 0 - we don't need it, 1 must surround both ends
      # if i==n-1:
      #   if count > countMax:
      #     countMax = count

  return countMax

N=1041
N=6
N=328

print(bin(N)[2:])
print solution(N)