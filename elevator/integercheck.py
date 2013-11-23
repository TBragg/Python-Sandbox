import os
import time

def integer_check():
	input = raw_input ('Input: ')
	try:
		input = int(input)
		return True
	except:
		return False

while not integer_check():
	print 'Not a valid input.'
	
print 'Yay! That was an integer!'
