#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
max diff that bigger num has bigger index
"""

DEBUG = False #turn this TRUE/False to turn ON/off for PyCharm debug; MUST turn off when submitted

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if DEBUG: from _hackerrank_.util import * ; redirectStdio2File()


def maxDifference22(a):
  n = len(a)
  import sys
  maxDiff = -sys.maxint
  for i in xrange(0,n):
    for j in xrange(i+1,n-1):
      if a[j]>a[i]:
        if a[j]-a[i]>maxDiff:
          maxDiff = a[j]-a[i]

  return maxDiff


def maxDifference(a):
  n = len(a)
  import sys
  maxDiff = -sys.maxint
  for i in xrange(n):
    for j in xrange(n):
      if a[i]>=a[j]:
        soLon=a[i]
        soNho=a[j]
        indexLon=i
        indexNho=j
      else:
        soLon=a[j]
        soNho=a[i]
        indexLon=j
        indexNho=i

      h = soLon-soNho
      indexOk = indexLon>indexNho
      if indexOk:
        if h>maxDiff:
          maxDiff=h

  return maxDiff

a = [7,9,5,6,3,2]
a = [2,3,10,2,4,8,1]
print(maxDifference(a))


