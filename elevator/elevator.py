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

def IntroScreen():
	os.system('clear')
	DisplayBuilding(0)
	input = raw_input('Please enter a floor number: ')

os.system('clear')
print 'Welcome to Taylor\'s Elevator Simulation Script(TM)'
time.sleep(2)

IntroScreen()

print 'Completed!'
