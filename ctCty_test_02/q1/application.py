#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
count number of number from n to m that don't have repeated digit
"""

a = [[1,20], [9,19]]
#output
# 19
# 10


a = [[7,8], [52,80], [57,64], [74,78]]
#output
# 2
# 26
# 8
# 4


def countNumbers(a):
  return countNumbers_01(a)


def countNumbers_00(a):
  for row in a:
    n = row[0]
    m = row[1]
    count = 0
    for i in xrange(n,m+1):
      s = str(i)
      checked = dict()
      ok=True
      for c in s:
        if c in checked:
          ok=False
          break
        else:
          checked[c]=1
      if ok:
        count+=1

    print(count)


def countNumbers_01(arr):
  for row in arr:
    n = row[0]
    m = row[1]
    count = 0
    for i in xrange(n,m+1):
      ok = True
      visited=dict()

      a = i
      while a>0:
        r = a % 10
        a = a // 10

        if r in visited:
          ok=False
          break
        else:
          visited[r]=1

      if ok:
        count+=1

    print(count)


countNumbers(a)
