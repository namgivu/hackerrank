#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()


import sys
N = int(sys.stdin.readline().strip())

st = []
maxVal = -sys.maxint
for _ in xrange(N):
  line = map(int, sys.stdin.readline().strip().split(' '))
  cmd = line[0]
  if cmd==1: val = line[1]

  if False: pass

  elif cmd==1: #push
    st.append(val)
    if val > maxVal:
      maxVal = val

  elif cmd==2: #pop
    val = st.pop()
    if val == maxVal:
      maxVal = max(st) if len(st)>0 else -sys.maxint

  elif cmd==3: #print max
    print(maxVal)


if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()
