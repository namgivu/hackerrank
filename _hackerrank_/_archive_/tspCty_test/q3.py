#!/usr/bin/env python2.7

"""
topic
Longest word in a sentence that has even length value
"""


def longestEvenWord(setence):
  words = setence.split(' ')
  import sys ; maxLength = -sys.maxint
  maxWord=None
  for word in words:
    l = len(word)
    if l % 2 == 0:
      if l>maxLength:
        maxLength = l
        maxWord = word
  return maxWord if maxWord is not None else '00'


s='It is a pleasant day today'
s='You can do it the way you like '
print longestEvenWord(s)
