#!/usr/bin/env python2.7

"""
https://codility.com/c/run/demo7W7G4Z-649#final-form
"""

A = [-1, 3, -4, 5, 1, -6, 2, 1]


def solution(A):
  sumLeft = 0
  sumRight = 0
  N = len(A)
  for i in xrange(1,N):
    sumRight += A[i]

  for i in xrange(0,N):
    P = i

    # print(sumLeft, P, A[P], sumRight)
    if sumLeft == sumRight:
      return P

    if i<N-1:
      sumLeft  += A[P]
      sumRight -= A[P+1]

  return -1


print solution(A)