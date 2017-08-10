#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/simple-text-editor
"""

DEBUG = False


#turn this on when debug to redirect stdin to file in PyCharm ref. https://stackoverflow.com/a/39482389/248616
if DEBUG: from _hackerrank_.util import * ; setupPycharmDebug()

import sys
Q = int(sys.stdin.readline().strip())
S = ''
history = []
for _ in xrange(Q):
  values = sys.stdin.readline().strip().split(' ')
  action=int(values[0])

  """
  1 append(W) - Append string W to the end of .
  2 delete(k) - Delete the last k characters of .
  3 print(k)  - Print the k-th character of .
  4 undo      - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.  
  """

  if False: pass

  #region handle action
  elif action==1:
    W = values[1]
    S += W
    history.append(dict(action=action, arg=W))

  elif action==2:
    k = int(values[1])
    deletedChars = S[-k:]#read last k characters ref. https://stackoverflow.com/a/7983848/248616
    S = S[:-k] #remove last k characters ref. https://stackoverflow.com/a/1798537/248616
    history.append(dict(action=action, arg=deletedChars))

  elif action==3:
    k = int(values[1])
    print(S[k-1])

  elif action==4:
    lastAction = history.pop()
    if False: pass

    elif lastAction['action']==1:
      lastW = lastAction['arg']
      S = S[:-len(lastW)] #delete last-added W ref. #ref. https://stackoverflow.com/a/1798537/248616

    elif lastAction['action']==2:
      deletedChars = lastAction['arg']
      S += deletedChars #add last-deleted W ref. #ref. https://stackoverflow.com/a/1798537/248616

  #endregion handle action

  # print('S=%s' % S)
  if DEBUG: from _hackerrank_.util import * ; flushOutput()
