from pygame import *

# Initializing pygame
init()

# Creating the screen
screen = display.set_mode((800, 600))

running = True
while running:
	for event in pygame.event.get():
		print(event)
