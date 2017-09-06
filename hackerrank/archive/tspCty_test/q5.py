#!/usr/bin/env python2.7

"""
topic
Given a string of < and > characters
Determine whether it is balanced or not
Also a messing question on counting the times the '>' occurs and cause an un-balance
"""


def balancedOrNot(expressions, maxReplacements):
  outputs=[]

  for i in xrange(0,len(expressions) ) :
    expression = expressions[i]
    maxReplacement = maxReplacements[i]

    s=[] #the check stack
    needFix=0
    for c in expression:
      if c=='<':
        s.append(c)
      elif c=='>':
        if len(s)>0:
          s.pop()
        else: #it is unbalanced to fix
          needFix+=1

    if len(s)>0:
      output=0

    elif len(s)==0:
      if needFix <= maxReplacement:
        output = 1
      else:
        output = 0

    outputs.append(output)

  return outputs


#region input
expressions=[
  '<>',
  '<>><',
]
maxReplacements=[
  1,
  0,
]

expressions=[
  '<>>>',
  '<>>>>',
]
maxReplacements=[
  2,
  2,
]
#endregion input


outputs = balancedOrNot(expressions, maxReplacements)
for o in outputs: print(o)
