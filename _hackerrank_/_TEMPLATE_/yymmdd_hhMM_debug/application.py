#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import * ; redirectStdio2File()

import sys
N = int(sys.stdin.readline().strip())

a = []
a = map(int, sys.stdin.readline().strip().split(' '))

print(N)
print(a)

if REDIRECT_STDIO_2_FILE: from _hackerrank_.util import *; flushOutput()
