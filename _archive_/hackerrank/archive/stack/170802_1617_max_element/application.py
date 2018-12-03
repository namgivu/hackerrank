#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/maximum-element
"""
import sys

stack = []
N = int(sys.stdin.readline())
for i in xrange(1,N+1):
  line = sys.stdin.readline().strip().split(' ')
  query = int(line[0])
  param = int(line[1]) if query==1 else None

  if False: pass
  elif query==1:
    stack.append(param)
  elif query==2:
    stack.pop()
  elif query==3:
    print(max(stack)) #TODO need a faster way to store the max value

  #print(stack)
