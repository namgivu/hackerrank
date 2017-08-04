#!/usr/bin/env python2.7

"""
DESC
A queue of people to use elevator
N people, people=weight+targetFloor
elevator= + weight limit + people limit
Count the stopping time of the elevator to serve the queue to their floors
"""


def solution(A, B, M, X, Y):
  # print(A) ; print(B) ; print(M) ; print(X, Y) ; print

  count=0

  n=len(A)
  curX=0
  curY=0
  floors=dict()

  for i in xrange(n):
    curX_next = curX + 1
    curY_next = curY + A[i]

    ok = curX_next<=X and curY_next<=Y

    if ok:
      curX = curX_next
      curY = curY_next
      floors[B[i]] = 1

    elif not ok:
      #run the elevator => count stop times and empty it after run
      count += len(floors.keys())+1

      curX=1
      curY=A[i]
      floors={}
      floors[B[i]] = 1

    # print(i, count, curX, curY, floors)
    pass

    #the last wave
    if i == n - 1:
      if len(floors.keys())>0:
        count += len(floors.keys()) + 1

  return count

#region input
pass

A = [40,40,100,80,20]
B = [3,3,2,2,3]
M = 3 ; X = 5 ; Y = 200

# A = [60,80,40]
# B = [2,3,5]
# M = 5 ; X = 2 ; Y = 200

pass
#endregion input
print(solution(A,B,M,X,Y))
