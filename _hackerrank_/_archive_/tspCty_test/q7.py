#!/usr/bin/env python2.7

"""
topic
A messing question on the core issue to solve - count the number of permutation
of a given string of digit. Each digit can be any of values from 0 to 9
"""


def findSimilar(a, b):
  sa = ''.join(sorted(str(a)))
  sb = ''.join(sorted(str(b)))


  def getCharDict(s):
    charDict = dict()
    for c in s:
      if c in charDict:
        charDict[c] += 1
      else:
        charDict[c] = 1
    return charDict


  count=dict(value=0)


  def countSimilar(digitDict, k, n, count):
    #TODO we fail with large input

    """Count recursively at digit at index k; k in [0,n-1] """
    if k>=n: #we reach the end => count +1
      count['value']+=1
      return

    for d in digitDict.keys():
      if digitDict[d]>0:
        digitDict[d] -= 1 #mark the used digit
        countSimilar(digitDict, k+1, n, count) #build next digit recursively at k+1 index
        digitDict[d] += 1 #un-mark/recover the used digit

  if sa==sb:
    countSimilar(digitDict=getCharDict(sa), k=0, n=len(sa), count=count)
  else:
    countSimilar(digitDict=getCharDict(sb),k=0, n=len(sb), count=count)

  return count['value']

a=1234
b=2341
print(findSimilar(a,b))
