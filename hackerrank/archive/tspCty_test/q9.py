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
    [i,j] = map(int, pair.strip().split(' '))
    a[i][j]=1
    a[j][i]=1

  #find connected regions
  visited=[]
  regions=[]
  for i in xrange(n):
    if i in visited: continue

    ##region start searching new connected-region from i
    pass

    #mark i as visited
    visited.append(i)

    #start the find from node i
    iConnected=[i]
    searchFrom=[i]
    while len(searchFrom)>0:
      newFound = []
      #find connected nodes near by
      for j in searchFrom:
        for h in xrange(n):
          if h not in visited:
            if a[j][h]==1:
              newFound.append(h)
              visited.append(h)
              iConnected.append(h)

      searchFrom = newFound

    pass
    ##endregion start searching new connected-region from i

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