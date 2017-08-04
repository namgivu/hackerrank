#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
Given i in the range [1..N], print sum of odd numbers <=i
"""


def calculate_00(a):
  for Ni in a:
    sum = 0
    for i in xrange(1,Ni+1):
      if i % 2 == 1:
        sum+=i

    print(sum)


def calculate_01(arr):
  for Ni in arr:
    a0 = 1
    aN = Ni
    n = (aN-a0)/2 + 1
    sum = (a0+aN) * n / 2
    print(sum)


def calculate(a):
  return calculate_01(a)


print 122

a=[1,2,3]
calculate(a)
