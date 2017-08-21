#!/usr/bin/env python2.7

"""
topic
Messing question on a graph that has multiple-value edge
And also, if (i,j)=x, and (j,k)=x then (i,k) is considered to be connected too i.e. (i,k)=x

A connected region at token=k is a region where all of its nodes are connected by edge weight to be k
Count the number of regions each pair of nodes can have
Pick out the maximum number among them, among the maximum candidates, pick out the one with maximum product ixj
"""


def  maxTokens(friends_nodes, friends_from, friends_to, friends_weight):
  """
  Pseudo code
  ===


  Graph definition (I mean the graph term in Graph Theory https://en.wikipedia.org/wiki/Graph_theory
  ---
  We build a graph with nodes and edges connect each pair of nodes
  Each edge has its weight value
  Between two nodes, we can have multiple edges with different weights


  We count the number of tokens for each pair of nodes (i,j) and then find the maximum target output
  ---
  - First we need to upgrade the graph as below step 'Graph upgrade'

  - We find the connected regions i.e. a region that contains nodes which are connected by their edges,
    AND all edges have the same weight values.
    As the result, with any node pair i and j, we can have multiple connected regions that contain them;
    each region has unique edge-weight value of its own

  - Number of tokens for node i and j = number of connected regions that contain them

  - We find the maximum number of tokens among the node-pairs
    We then pick out the pair that has the maximum product

  - Output the maximum product

  Graph upgrade
  ---
  - The target:
    We create edges to connect two nodes which are connected indirectly
    i.e. in our graph, any indirectly-connected pair of nodes will be connected directly
    This will help us to find the connected-region easily using 2d-array

  """
  return 122


friends_nodes=4
print maxTokens()