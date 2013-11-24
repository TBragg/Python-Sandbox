#!/usr/bin/python
# Filename: elevator.py

import os
import time
import ichk

BUILDING_HEIGHT = 20

def showBuilding(floor):
	os.system('clear')
	for x in range(BUILDING_HEIGHT,0,-1):
		if x==(floor):
			print '||----[0]----||', x
		else:
			print '||-----------||', x 

def getFloorChoice():
	while True:
		input = raw_input('Please enter your floor choice: ')
		if ichk.isInt(input) and int(input)<=BUILDING_HEIGHT:
			break	
	floor = int(input)+1
	return floor

def goToFloor(floor):
	for x in range(1,floor):
		showBuilding(x)
		time.sleep(.5)

# End of elevator.py