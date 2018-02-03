#!/usr/bin/env python3


class SomeClass:

  def __init__(self): pass

  some_field=''

  @classmethod
  def some_method(cls):
    cls.some_field = 'set by some_method()'


a = SomeClass()
a.some_field = 'set by a.some_field'

SomeClass.some_field = 'update by SomeClass.some_field'

print(a.some_field)
print(SomeClass.some_field)
