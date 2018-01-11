#!/usr/bin/env python3
import sys


def someMethod():
    functionNameAsString = sys._getframe().f_code.co_name
    return functionNameAsString


print(someMethod())
