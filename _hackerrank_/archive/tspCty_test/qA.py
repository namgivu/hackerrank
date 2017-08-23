#!/usr/bin/env python2.7

"""
topic
From all suffixes sub-string of a given string,
find the max length of prefix-matching character between the original string with those sub-strings
"""


#TODO we fail with large input

def stringSimilarity(inputs):
  outputs=[]


  def countSimilar(s,t):
    count=0
    n = min(len(s),len(t))
    for i in xrange(n):
      if s[i]!=t[i]:
        return count
      else:
        count+=1
    return count


  for s in inputs:
    cs=0 #cs stands for count similar
    for i in xrange(len(s)):
      t = s[i:] #get suffix with len=i+1
      cs += countSimilar(s,t)
      # print s, t, cs

    outputs.append(cs)

  return outputs


inputs=[
  # 'abcdef',
  'ababaa',
]
print(stringSimilarity(inputs))
