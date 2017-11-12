#!/usr/bin/env python3

dataArr = [0, 1, 2, 3, 4, 5, 6]

curr = nxt = last = None
start = None


def process(curr, nxt, msg):
  print(curr, nxt, msg)
  print('process %s' % curr)


for cursor in dataArr:
  msg = cursor #just alias

  if not curr:
    curr = msg
    start = curr
  elif curr and not nxt:
    nxt = msg

  else:
    process(curr, nxt, msg)

    curr = nxt
    nxt = msg

  last = msg

#process 'nxt, last' as 'curr, nxt'
#process 'last, nil' as 'curr, nxt'
process(curr, nxt, None)
process(nxt, None, None)

print
print(start, last)
