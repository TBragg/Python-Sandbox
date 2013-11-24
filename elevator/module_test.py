#!/usr/bin/python

__file__	= "module_test.py"
__author__	= "Taylor Bragg"

import sys
import mymodule
import ichk

mymodule.sayhi()
print 'Version',mymodule.version

#input = raw_input('Input: ')

while True:
	input = raw_input('Input: ')
	if ichk.isInt(input):
		break
