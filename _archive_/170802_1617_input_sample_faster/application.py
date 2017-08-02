#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/maximum-element
"""
import sys

N = int(sys.stdin.readline())

for i in xrange(1,N+1):
  line = sys.stdin.readline().strip().split(' ')
  i = int(line[0])
  j = int(line[1])
