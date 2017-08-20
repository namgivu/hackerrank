#!/usr/bin/env python2.7

"""
topic
Given a graph, find the connected regions
Compute the value of a formula based on the regions' lengths
"""


def minimalCost(n, pairs):
  #region build graph to 2d-array a
  a=[]
  for i in xrange(n):
    row=[]
    for j in xrange(n):
      row.append(0)
    a.append(row)
  #endregion build graph to 2d-array a

  #load the graph
  for pair in pairs:
    split = pair.split(' ')
    i = int(split[0])-1
    j = int(split[1])-1
    a[i][j]=1
    a[j][i]=1

  #find connected regions
  visited=[]
  regions=[]
  for i in xrange(n):
    if i not in visited:
      visited.append(i) #mark i as visited

      #start the find from node i
      iConnected=[i]
      b=[i] ;
      while len(b)>0:
        #find connected node nearby
        newFound = []
        for j in b:
          for h in xrange(n):
            if h not in visited:
              if a[j][h]==1:
                newFound.append(h)
                visited.append(h)
                iConnected.append(h)
        b = newFound
      # print iConnected
      regions.append(iConnected)


  #compute output
  count=0
  import math
  for region in regions:
    count += math.ceil(
      math.sqrt(len(region))
    )
  return int(count)


n=4
pairs=['1 2', '1 4']

n=8
pairs=['8 1', '5 8', '7 3', '8 6',]

print minimalCost(n, pairs)