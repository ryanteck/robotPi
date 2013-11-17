#The code for the robot
import network
import sys

def heard(phrase):
	print phrase

print "Chat Program"

network.wait(whenHearCall=heard)

print "Conected!"  
while True:
	pass
