#!/usr/bin/python
# Filename: atm.py

import ichk

ATM_BALANCE = 1234.56
PIN_NUMBER = 1234

def login():
	while True:
		input = raw_input('Please enter your PIN: ')
		if ichk.isInt(input) and int(input)==PIN_NUMBER:
			break
		else:
			print 'Incorrect PIN. Please try again.'

def showBalance():
	print "Your balance is: ", ATM_BALANCE

print "Welcome to Taylor's ATM"

# End of atm.py