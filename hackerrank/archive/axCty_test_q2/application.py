#!/usr/bin/env python2.7

"""
Implement a circular queue of integers of user-specified size using a simple array.
Provide routines to initialize(), enqueue() and dequeue() the queue.
Make it thread safe.

Please do not to use existing class libraries for this question. Thanks!
"""

REDIRECT_STDIO_2_FILE = False
REDIRECT_STDIO_2_FILE = True

#turn this on when debug to redirect stdin/stdout to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if REDIRECT_STDIO_2_FILE: from hackerrank.util import * ; redirectStdio2File()


def plainSolution():
  a=[]
  n = 0 #queue size
  headNode=None #queue head

  import sys
  N = int(sys.stdin.readline().strip())
  for _ in xrange(N):
    [cv, note] = sys.stdin.readline().strip().split('#') #cv stands for command-value
    line = map(int, cv.strip().split(' '))

    command = value = None
    if len(line)==2:
      [command, value]=line
    else:
      command = line[0]

    # print(command,value)

    if False: pass

    #init queue
    elif command==0:
      n = value if value>=0 else 0
      a = [None]*n
      headNode = -1

    #enqueue
    elif command==1:
      i = value
      if headNode+1>=n: #out of queue size
        raise Exception('Out of queue size n=%s' % n)
      headNode += 1
      a[headNode] = i

    #dequeue
    elif command==2:
      a[headNode]=None
      headNode = max(headNode-1, -1)

    elif command==3:
      print(a)


'''
the python code
'''


'''
sample input
10
0 6   #0-init queue size=6
3     #3-print
1 22  #1-enqueue value=22
3     #3-print
1 333 #1-enqueue value=333
3     #3-print
2     #2-dequeue
3     #3-print
2     #2-dequeue
3     #3-print

sample output
[None, None, None, None, None, None]
[22, None, None, None, None, None]
[22, 333, None, None, None, None]
[22, None, None, None, None, None]
[None, None, None, None, None, None]

'''


def oopSolution(): #oop stands for object-oriented programming
  #region helper
  pass

  class Queue:
    a = []
    n = 0
    headNode = -1

    from multiprocessing import Lock
    mutext = Lock() #making it thread-safe ref. https://stackoverflow.com/a/3311157/248616

    def __init__(self, size=0):
      return self.initialize(size)

    def __repr__(self):
      return str(self.a)

    def initialize(self, size):
      with self.mutext: #making it thread-safe ref. https://stackoverflow.com/a/3311157/248616
        self.n = size if size >= 1 else 0
        self.a = [None] * self.n
        self.headNode = -1

    def enqueue(self, value):
      with self.mutext: #making it thread-safe ref. https://stackoverflow.com/a/3311157/248616
        if self.headNode + 1 >= self.n:  # out of queue size
          raise Exception('Out of queue size n=%s' % self.n)

        self.headNode += 1
        self.a[self.headNode] = value

    def dequeue(self):
      with self.mutext: #making it thread-safe ref. https://stackoverflow.com/a/3311157/248616
        self.a[self.headNode] = None
        self.headNode = max(self.headNode - 1, -1)

  pass
  #endregion helper

  q = Queue()

  import sys
  N = int(sys.stdin.readline().strip())
  for _ in xrange(N):
    [cv, note] = sys.stdin.readline().strip().split('#') #cv stands for command-value
    line = map(int, cv.strip().split(' '))

    command = value = None
    if len(line)==2:
      [command, value]=line
    else:
      command = line[0]

    # print(command,value)

    if False: pass

    #init queue
    elif command==0:
      q.initialize(size=value)

    #enqueue
    elif command==1:
      q.enqueue(value)

    #dequeue
    elif command==2:
      q.dequeue()

    elif command==3:
      print(q)

  pass

oopSolution()
#plainSolution()

if REDIRECT_STDIO_2_FILE: from hackerrank.util import *; flushOutput()
