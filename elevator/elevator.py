#!/usr/bin/python
# Filename: elevator.py

BUILDING_HEIGHT = 20

def showBuilding(floor):
	for x in range(BUILDING_HEIGHT,0,-1):
		if x==(floor+1):
			print '||----[0]----||', x
		else:
			print '||-----------||', x 

# End of elevator.py