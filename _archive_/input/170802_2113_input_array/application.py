#!/usr/bin/env python2.7

"""https://www.hackerrank.com/challenges/equal-stacks"""

n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

print(n1, n2, n3)
print(h1, h2, h3)