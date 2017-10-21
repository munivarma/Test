#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

class MyError(Exception):
    def __init__(self, value):
        self.error_string = value

    def __str__(self):
        return eval(repr(self.error_string))

try:
    script, arg1 = sys.argv

except ValueError:     
    raise MyError, "Not enough arguments"
