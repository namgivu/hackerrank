#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/maximum-element
"""
import fileinput
lines = fileinput.input()

stack = []
N = int(lines[0])
for i in xrange(1,N+1):
  line = lines[i].strip().split(' ')
  query = int(line[0])
  param = int(line[1]) if query==1 else None

  if False: pass
  elif query==1:
    stack.append(param)
  elif query==2:
    stack.pop()
  elif query==3:
    print(max(stack))

  print(stack)
