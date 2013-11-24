#!/usr/bin/python
# Filename: atm.py

import ichk

ATM_BALANCE = 1234.56
PIN_NUMBER = 1234
LOGIN_TRIES = 4

def login():
	count = 0
	while True:
		count+=1
		input = raw_input('Please enter your PIN: ')
		if ichk.isInt(input) and int(input)==PIN_NUMBER:
			break
		else if count == LOGIN_TRIES:
			print 'You've exceeded the number of login attempts. Goodbye.'
		else:
			print 'Incorrect PIN. Please try again.'

def showBalance():
	print "Your balance is: ", ATM_BALANCE

print "Welcome to Taylor's ATM"

# End of atm.py