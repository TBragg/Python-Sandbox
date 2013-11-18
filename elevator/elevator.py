import os
import time

BUILDING_HEIGHT = 20

# Function definitions
def ElevatorSimulator(e,f):
	os.system('clear')
	print 'Taylor\'s Elevator Simulation Script(TM)'
	print ''
	for x in range(0,f):
		if x==e:
			print '*----[0]----*'
		else:
			print '*-----------*'

def DisplayBuilding(floor):
	for x in range(BUILDING_HEIGHT,0,-1):
		if x==(floor+1):
			print '||----[0]----||', x
		else:
			print '||-----------||', x 

# Still need to work on confirming integer value
def IntroScreen():
	os.system('clear')
	DisplayBuilding(0)
	input = raw_input('Please enter a floor number: ')
	while(isinstance(input, int) == False):
		print("That's not an int!")
		input = raw_input('Please enter a valid floor number: ')

os.system('clear')
print 'Welcome to Taylor\'s Elevator Simulation Script(TM)'
time.sleep(2)

floor_selection = IntroScreen()

print 'Completed!'
