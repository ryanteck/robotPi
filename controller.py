#Code for the controller
import network
import sys
import pygame
from pygame.locals import *
import time

network.port(int(sys.argv[2]))

def heard(phrase):
	#Do nothing
	print "I heard something, its broke"



network.call(sys.argv[1], whenHearCall=heard)

print "Online"


pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Robot Controller')

#We need colors, I think Raspberry Red and Raspberry Green would be best.
raspberryred = (214,38,79)
raspberrygreen = (96,178,46)
white = (250,250,250)
black = (0,0,0)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(white)

screen.blit(background, (0, 0))

#Up
pygame.draw.rect(screen, raspberryred, (374,217,128,128), 0)

#L,D,R
pygame.draw.rect(screen, raspberryred, (241,350,128,128), 0)
pygame.draw.rect(screen, raspberryred, (374,350,128,128), 0)
pygame.draw.rect(screen, raspberryred, (507,350,128,128), 0)



pygame.display.flip()
forward = 0
backwards = 0
left = 0
right = 0

forwardon = 0
backwardson = 0
lefton = 0
righton = 0

while True:
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_RIGHT]:
		pygame.draw.rect(screen, raspberrygreen, (507,350,128,128), 0)
 		pygame.display.flip()
		right = 1
	else:
		pygame.draw.rect(screen, raspberryred, (507,350,128,128),0)
                pygame.display.flip()
		right = 0

	if keystate[pygame.K_LEFT]:
		pygame.draw.rect(screen, raspberrygreen, (241,350,128,128), 0)
		pygame.display.flip()
		left = 1
	else:
		pygame.draw.rect(screen, raspberryred, (241,350,128,128), 0)
		pygame.display.flip()
		left = 0	

	if keystate[pygame.K_UP]:
		pygame.draw.rect(screen, raspberrygreen, (374,217,128,128), 0)
		pygame.display.flip()
		forward = 1
	else:
		pygame.draw.rect(screen, raspberryred, (374,217,128,128), 0)
		pygame.display.flip()
		forward = 0

	if keystate[pygame.K_DOWN]:
		pygame.draw.rect(screen, raspberrygreen, (374,350,128,128), 0)
		pygame.display.flip()
		backwards = 1
		
	else:
		pygame.draw.rect(screen, raspberryred, (374,350,128,128), 0)
		pygame.display.flip()
		backwards = 0
	
	#and now process the network code, left and right are first, forwards is second and then backwards is last.
	if (left == 1 and lefton == 0):
		network.say("l")
		lefton = 1
	elif (right == 1 and righton == 0):
		network.say("r")
		righton = 1
	elif (forward == 1 and forwardon == 0):
		network.say("f")
		forwardon = 1
	elif (backwards == 1 and backwardson == 0):
		network.say("b")
		backwardson = 1

	if(lefton ==1):
		if(left == 0):
			network.say("ls")
			lefton = 0

	if(forwardon ==1):
		if(forward == 0):
			network.say("fs")
			forwardon = 0

	if(righton ==1):
		if(right == 0):
			network.say("rs")
			righton = 0

	if(backwardson ==1):
		if(backwards == 0):
			network.say("bs")
			backwardson = 0



	pygame.event.pump() # process event queue
	#time.sleep(0.1)
