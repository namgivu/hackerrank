"""
https://www.hackerrank.com/challenges/30-hello-world/problem
"""
#!/usr/bin/env python2.7

REDIRECT_STDIO_2_FILE = False # turn this on when submit to hackerrank
REDIRECT_STDIO_2_FILE = True  # turn this on when run local

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()


import sys
s = sys.stdin.readline().strip()

print(f'''
Hello, World.
{s}
'''.strip())


if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()
