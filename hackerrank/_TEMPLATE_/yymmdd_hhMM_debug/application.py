"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""

REDIRECT_STDIO_2_FILE = False # turn this on when submit to hackerrank
REDIRECT_STDIO_2_FILE = True  # turn this on when run local

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()


import sys
N = int(sys.stdin.readline().strip())
a = map(int, sys.stdin.readline().strip().split(' ')); a = list(a)

print(N)
print(a)


if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()
