#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
number of path
loan mang 2 chieu
"""

DEBUG = False #turn this TRUE/False to turn ON/off for PyCharm debug; MUST turn off when submitted

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if DEBUG: from _hackerrank_.util import * ; setupPycharmDebug()


a = [
  [1,1,1,1],
  [1,1,1,1],
  [1,1,1,1],
]
a = [
  [1,0],
  [0,1],
]


def numberOfPaths (a):
  count=0
  rows = len(a)
  cols = len(a[0]) if rows>0 else 0
  # print('M=%s' % rows) ; print('N=%s' % cols)

  i0=0 ; j0=0
  P = [
    [i0,j0]
  ]
  M = [
    [0,1],
    [1,0],
  ]
  while True:
    T=[]

    #go from every point in P
    for p in P:
      #mark as we has visited it
      a[p[0]][p[1]]=-1

      #go right or down
      for m in M:
        pNew = [p[0]+m[0], p[1]+m[1]]
        if (pNew[0]>=0 and pNew[0]<rows) and (pNew[1]>=0 and pNew[1]<cols):
          # print pNew, pNew[0]<rows, rows
          if a[pNew[0]][pNew[1]]==1:
            T.append(pNew)

          #reach target
          if pNew[0]==rows-1 and pNew[1]==cols-1:
            count+=1

    # print P ; print T ; print
    if len(T)==0:
      break
    else:
      P=T
  return count


print numberOfPaths(a)
