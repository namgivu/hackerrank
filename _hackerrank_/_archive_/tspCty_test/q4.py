#!/usr/bin/env python2.7

"""
topic
Print out the pascal triangle given its height as k
"""


def pascalTriangle(k):
  a = [1,1] #start from k=2
  print('1')
  print('1 1')
  for i in xrange(k-2):
    b=[1]
    for j in xrange(1,len(a)):
      b.append(a[j]+a[j-1])
    b.append(1)

    a=b
    print(' '.join(str(x) for x in a))

pascalTriangle(4)
