import os
import time

# Function definitions
def displayFloors(person,floors):
	os.system('clear')
	for x in range(0,floors):
		if x==person:
			print '*-----0-----*'
		else:
			print '*-----------*'

os.system('clear')

print 'Starting the Elevator Simulation Script(TM)'

time.sleep(5)

displayFloors(20)
