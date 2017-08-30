#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import * ; redirectStdio2File()


TRACE=False
import sys
Q = int(sys.stdin.readline().strip())



def countOp(N, currCount):
  if N<=3:
    if TRACE: trace.append('reach 3')
    return N+currCount

  #region find N=a*b and abMax
  import math
  sqN = int(math.sqrt(N))
  i=sqN
  abMax=-1
  while i<N:
    if N%i == 0:
      abMax=max(i, N/i)
      break
    i+=1
  #endregion find N=a*b and abMax

  if abMax>0:
    if TRACE: trace.append('abMax=%s' % abMax)
    return countOp(abMax, currCount+1)
  else: #N is prime
    if TRACE: trace.append('-1')
    return countOp(N-1, currCount+1)


trace=[]

for _ in xrange(Q):
  N = int(sys.stdin.readline().strip())
  trace=[]
  print(countOp(N,0))
  if TRACE: print(trace)


if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import *; flushOutput()

# 7
# ['abMax=1369', 'abMax=37', '-1', 'abMax=6', 'abMax=2', 'reach 3']
# 966514
# 1369 x 706
# 37 x 37
#
