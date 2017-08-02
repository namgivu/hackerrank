#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/maximum-element
"""
import sys

stack = []

N = int(sys.stdin.readline())
for i in xrange(N):
  line = sys.stdin.readline().strip().split()
  if not line: continue
  query = int(line[0])
  param = line[1] if query==1 else None

  if False: pass
  elif query==1:
    stack.append(param)
  elif query==2:
    stack.pop()
  elif query==3:
    print(max(stack))
