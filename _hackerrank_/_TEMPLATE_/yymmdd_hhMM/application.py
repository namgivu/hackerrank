#!/usr/bin/env python2.7

"""
https://www.hackerrank.com/challenges/YOUR-TOPIC
"""


def demoArray():
  """
  demo [n:] means take out the EXACT 'n' items
  demo [:n] means take ALL EXCEPT the 'n' items
  n>0       means start from the left
  n<0       means start from the right
  """

  a = [1,22,333, 'a','bb','ccc']
  print(a[2])  #item at index=2 from the left
  print(a[2:]) #only     the first two items
  print(a[:2]) #all BUT  the first two items

  print(a[-2]) #item at index=2 from the right
  print(a[-2:]) #only     the last two items
  print(a[:-2]) #all BUT  the first two items


demoArray()
