# Document says pygame is the top, pygame.local uses all the sub parts.
# Note: anything in pygame should start like this.
import pygame
from pygame.locals import *


# 2 - Initialize the game
pygame.init()
width, height = 600, 800
screen = pygame.display.set_mode((width, height))

# Names the window
pygame.display.set_caption('Hello')

# the fps (in game time)
clock = pygame.time.Clock()


# Game loop (the main loop)

crashed = False

while not crashed:
# Basic events (mouse, key press / frame)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
# This is the event in foreground
    pygame.display.update()
# Fps
    clock.tick(30)

pygame.quit()
quit()
