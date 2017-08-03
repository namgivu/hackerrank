#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
inverse bit of 10-base number and print the result in 10-base
"""

DEBUG = False #turn this TRUE/False to turn ON/off for PyCharm debug; MUST turn off when submitted

#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if DEBUG: from util import * ; setupPycharmDebug()


def getIntegerComplement(a):
  b = bin(a)[2:]
  s=''
  for c in b:
    if c=='0':
      s+='1'
    else:
      s+='0'
  t = int(s,2)
  return t

a = 50
a = 100
print getIntegerComplement(a)
