#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

import sys
N = int(sys.stdin.readline())

def matched(_c, c):
  return False \
         or (_c=='(' and c==')') \
         or (_c=='[' and c==']') \
         or (_c=='{' and c=='}') \
         or False


def check(s):
  ok=True
  stack = []
  _c = None
  for i in xrange(len(s)):
    c = s[i]

    if c in [']',')','}']:
      #region handle closing
      _c = stack.pop() if len(stack)>0 else None
      if not matched(_c, c):
        ok=False
        break
      #endregion handle closing

    else:
      stack.append(c)

  return 'YES' if ok else 'NO'

for i in xrange(N):
  s = sys.stdin.readline().strip()
  print(check(s))
