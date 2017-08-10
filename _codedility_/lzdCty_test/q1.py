#!/usr/bin/env python2.7

"""
DESC
Find substring of a string that 1) has at least 01 upper case, and 2) has NO digit
"""


def solution(S):

  digits=[]
  for i in xrange(10):
    digits.append(str(i))

  import string
  upperChars = string.uppercase[:26]


  #region get sub string separated by digits
  subStringList = []
  s = ''
  n=len(S)
  for i in xrange(n):
    c=S[i]

    if c not in digits:
      s+=c

    else:
      if len(s)>0:
        subStringList.append(s)
        s=[]

    if i==n-1:
      if len(s)>0:
        subStringList.append(s)
  #endregion get sub string separated by digits


  lenMax=-1

  for s in subStringList:
    valid=False

    #region check if an uppercase exists
    for c in s:
      if c in upperChars:
        valid=True
        break
    #endregion check if an uppercase exists

    if valid:
      l=len(s)
      if l>lenMax:
        lenMax=l

  #print(subStringList) ; print(lenMax)

  return lenMax


S = 'a0bb'
S = 'a0Ba'

print(solution(S))
