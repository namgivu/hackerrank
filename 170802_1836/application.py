#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/equal-stacks
"""

import sys
n123 = sys.stdin.readline().strip().split(' ')
n1 = int(n123[0])
n2 = int(n123[0])
n3 = int(n123[0])


def getStack(heights):
  stack = []
  n = len(heights)
  for i in xrange(n):
    j = n-1-i
    stack.append(int(heights[j]))
  return stack

n1Heights = getStack(sys.stdin.readline().strip().split(' '))
n2Heights = getStack(sys.stdin.readline().strip().split(' '))
n3Heights = getStack(sys.stdin.readline().strip().split(' '))

#print(n1Heights) ; print(n2Heights) ; print(n3Heights)


def trackSum(heights, d):
  s = 0
  for height in heights:
    s += height
    d[s]=d[s]+1 if d.has_key(s) else 1

d = dict()
trackSum(n1Heights, d)
trackSum(n2Heights, d)
trackSum(n3Heights, d)

maxHeight=-sys.maxint
for height,count in d.items():
  if count==3:
    # print('%s %s' % (height, count) )
    if height>maxHeight:
      maxHeight=height

# print(d)
maxHeight = 0 if maxHeight==-sys.maxint else maxHeight
print(maxHeight)
