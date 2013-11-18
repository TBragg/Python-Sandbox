import os
import time

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

os.system('clear')
print 'Starting the Elevator Simulation Script(TM)'
time.sleep(2)

floors = 20
for elevator in range(0,floors):
	ElevatorSimulator(elevator,floors)
	time.sleep(0.5)
print 'Completed!'
