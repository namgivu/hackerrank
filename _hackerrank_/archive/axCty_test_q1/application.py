#!/usr/bin/env python2.7

"""
Write me a function that receives three integer inputs for the lengths of the sides of a triangle
and returns one of four values to determine the triangle type
(1=scalene, 2=isosceles, 3=equilateral, 4=error).

Generate test cases for the function assuming another developer coded the function

Notes
How to validate 3 sides of a triangle i.e. a, b,c?
- All below condition must be true
  a + b > c
  a + c > b
  b + c > a

  ref. https://stackoverflow.com/a/19835249/248616
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()

'''
the python code
'''

'''
sample input
5
1 2 3       #output=0 error
3 4 5       #output=1 scalene
1 6 5.568   #output=1 scalene ref. http://www.calculator.net/triangle-calculator.html?vc=60&vx=1&vy=6&va=&vz=&vb=&angleunits=d&x=74&y=15
6 6 3.106   #output=2 isosceles ref. http://www.calculator.net/triangle-calculator.html?vc=30&vx=6&vy=6&va=&vz=&vb=&angleunits=d&x=59&y=11
6 6 6       #output=3 equilateral

sample output
0
1
1
2
3
'''


#region helper methods
def isTriangle(a,b,c):
  return True \
         and a + b > c \
         and b + c > a \
         and c + a > b


def isEquilateral(a,b,c):
  return a==b==c


def isIsosceles(a,b,c):
  return True and \
         a==b or b==c or c==a


def isScalene(a,b,c):
  return isTriangle(a,b,c)


#endregion helper methods


import sys
N = int(sys.stdin.readline().strip())
for _ in xrange(N):
  [abc, note] = sys.stdin.readline().strip().split('#')
  [a,b,c] = map(float, abc.strip().split(' '))
  # print(a,b,c)

  if False: pass
  elif not isTriangle(a,b,c): print(0)
  elif isEquilateral(a,b,c):  print(3)
  elif isIsosceles(a,b,c):    print(2)
  elif isScalene(a,b,c):      print(1)

if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()
