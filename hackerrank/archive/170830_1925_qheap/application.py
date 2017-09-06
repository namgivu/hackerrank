#!/usr/bin/env python2.7

"""
ref.
https://www.hackerrank.com/challenges/qheap1?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

util.
https://docs.python.org/2/library/heapq.html
"""

#TODO we failed with big input

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import * ; redirectStdio2File()


import sys
Q = int(sys.stdin.readline().strip())

#region heap data structure
from heapq import * #ref. https://docs.python.org/2/library/heapq.html
h=[]


def heapdel(h, value):
  h.remove(value)
  heapify(h)


# endregion heap data structure

for _ in xrange(Q):
  #read cmd
  line = map(int, sys.stdin.readline().strip().split(' '))
  cmd = line[0]
  if cmd!=3: val = line[1]

  #run cmd
  if False: pass
  elif cmd==3: #print
    minValue = heappop(h)
    heappush(h, minValue)
    print(minValue) #pop min value and re-push it

  elif cmd==1: #add
    heappush(h, val)

  elif cmd==2: #delete
    heapdel(h, val)


if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import *; flushOutput()
