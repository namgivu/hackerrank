#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()


import sys
n = int(sys.stdin.readline().strip())

a=[]
for i in xrange(n):
  ai=[]
  for j in xrange(n): ai.append(0)
  a.append(ai)


#region define next move data
"""
0 8 0 1 0
7 0 0 0 2
0 0 x 0 0
6 0 0 0 3
0 5 0 4 0
"""

allNextMove = [
  [-2, 1],
  [-1, 2],
  [ 1, 2],
  [ 2, 1],
  [ 2,-1],
  [ 1,-2],
  [-1,-2],
  [-2,-1],
]
#endregion define next move data


def print2DArray(a,n):
  for i in xrange(n):
    print(' '.join([str(aij) for aij in a[i]]))


def searchAt(i,j):
  global a, n, count
  # print i,j; print2DArray(a,n)

  if count == n:
    print2DArray(a,n)
    import sys ; sys.exit()

  for nextMove in allNextMove:
    i_next = i + nextMove[0]
    j_next = j + nextMove[1]

    #try the next move
    if True \
      and i_next in xrange(n) \
      and j_next in xrange(n) \
      and a[i_next][j_next]==0 \
    :
      a[i_next][j_next] = 1
      count+=1
      searchAt(i_next, j_next)
      count-=1
      a[i_next][j_next] = 0

for i in xrange(n):
  for j in xrange(n):
    count = 1
    a[i][j]=1
    searchAt(i,j)
    a[i][j]=0

print('Not possible')

if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()

