import pygame, sys, time, math, random

from pygame.locals import *

pygame.init()

XSCREEN = 500
YSCREEN = 500

DISPLAYSURF = pygame.display.set_mode((XSCREEN, YSCREEN))

pygame.display.set_caption('Hello World!')

# setup colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# draw on the surface object
DISPLAYSURF.fill(BLACK)

x = math.floor(XSCREEN / 2) #Centered and floor value
y = math.floor(YSCREEN / 2) #Centered and floor value

done = False

while not done: # main game loop  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  DISPLAYSURF.fill(BLACK)

  pygame.draw.circle(DISPLAYSURF, GREEN, (x , y), 10, 0)

  # UPDATE THE SCREEN
  pygame.display.flip()