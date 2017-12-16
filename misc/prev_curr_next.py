#!/usr/bin/env python3

dataArr = [0, 1, 2, 3, 4, 5, 6]

prev = curr = last = None
start = None


def process(curr, nxt, msg):
  print(curr, nxt, msg)
  print('process %s' % curr)


for cursor in dataArr:
  nxt = cursor #just alias

  if not prev:
    prev = nxt
    start = prev
  elif prev and not curr:
    curr = nxt

  else:
    process(prev, curr, nxt)

    prev = curr
    curr = nxt

  last = nxt

#handle the last value of prev & curr
process(prev, curr, None)
process(curr, None, None)

print
print(start, last)
