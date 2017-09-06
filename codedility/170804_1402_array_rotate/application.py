#!/usr/bin/env python2.7

"""
https://codility.com/c/run/trainingAYEX7G-UE7
"""


def solution(A, K):
  n = len(A)
  for i in xrange(n):
    A.append(A[i])

  K = K % n if n>0 else 0
  print(A) ; print(K)

  B = []
  for i in xrange(n-K, n-K+n):
    B.append(A[i])

  return B

#region input

A = [3, 8, 9, 7, 6]
K = 3

A = []
K = 22

A = [1,2]
K = 1

A = [1,2]
K = 0

#endregion input

print(solution(A,K))
