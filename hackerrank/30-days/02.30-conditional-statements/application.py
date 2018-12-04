"""
https://www.hackerrank.com/challenges/30-hello-world/problem
"""
#!/usr/bin/env python2.7

REDIRECT_STDIO_2_FILE = False # turn this on when submit to hackerrank
REDIRECT_STDIO_2_FILE = True  # turn this on when run local

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()


'''
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
'''
import sys
n = int(sys.stdin.readline().strip())

w='Weird'; nw='Not Weird'
if n % 2 == 1:     print(w)
if n % 2 == 0:
    if 2<=n<=5:    print(nw)
    elif 6<=n<=20: print(w)
    else:          print(nw)


if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()
