#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/waiter
"""

DEBUG = True #turn this TRUE/False to turn ON/off for PyCharm debug; MUST turn off when submitted
DEBUG = False #turn this TRUE/False to turn ON/off for PyCharm debug; MUST turn off when submitted

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if DEBUG: from hackerrank.util import * ; redirectStdio2File()

import sys
N,Q = map(int, sys.stdin.readline().strip().split(' '))
a = map(int, sys.stdin.readline().strip().split(' '))


def primeList(n):
  #ref. https://stackoverflow.com/a/3886074/248616

  #http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
  """ Returns  a list of primes < n """
  sieve = [True] * n
  for i in xrange(3, int(n ** 0.5) + 1, 2):
    if sieve[i]:
      sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
  return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


primes = primeList(max(a))
b=[]
bALL=[]
for i in xrange(Q):
  #Q required is larger than the maximum prime we need to work with the plates => no more plate for Bi pile will be found
  if i>=len(primes): break

  p = primes[i]
  a_ = []
  b = []
  for _ in xrange(len(a)):
    ai = a.pop()
    if ai % p == 0:
      b.append(ai)
    else:
      a_.append(ai)
  a = a_
  bALL.append(b)


def printStack(s):
  for _ in xrange(len(s)):
    print(s.pop())


for b in bALL:
  printStack(b)
printStack(a)
