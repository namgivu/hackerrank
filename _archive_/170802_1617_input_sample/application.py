#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/maximum-element
"""
import fileinput
lines = fileinput.input()

N = int(lines[0])
for i in xrange(1,N+1):
  line = lines[i].split(' ')
  query = int(line[0])
  param = line[1] if query==1 else None
  print(query)
