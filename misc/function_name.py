#!/usr/bin/env python3
import sys


def someMethod():
    #ref. https://stackoverflow.com/a/15725912/248616
    functionNameAsString = sys._getframe().f_code.co_name
    return functionNameAsString


print(someMethod())
