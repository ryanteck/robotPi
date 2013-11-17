#Code for the controller
import network
import sys
import pygame
from pygame.locals import *
import time


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
	if (left == 1):
		network.say("l")
	elif (right == 1):
		network.say("r")
	elif (forward == 1):
		network.say("f")
	elif (backwards == 1):
		network.say("b")

	pygame.event.pump() # process event queue
	time.sleep(0.1)
