# Document says pygame is the top, pygame.local uses all the sub parts.
# Note: anything in pygame should start like this.
import pygame
from pygame.locals import *


# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))