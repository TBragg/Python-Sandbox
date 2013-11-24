#!/usr/bin/python

import atm

success = atm.login()

if success:
	atm.showBalance()