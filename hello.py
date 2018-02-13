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
DISPLAYSURF.fill(WHITE)

x = XSCREEN / 2
y = YSCREEN / 2
x_vector = random.randrange(-15,6)
y_vector = random.randrange(-25,26)
done = False

while not done: # main game loop  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  DISPLAYSURF.fill(WHITE)

  x = math.floor(x + x_vector)
  y = math.floor(y + y_vector)
  pygame.draw.circle(DISPLAYSURF, GREEN, (x , y), 10, 0)

  if (x > XSCREEN):
    x_vector *= -1
    x = XSCREEN - 1
  elif (y > YSCREEN):
    y_vector *= -1
    y = YSCREEN - 1
  elif (x < 0):
    x_vector *= -1
    x = 1
  elif (y < 0):
    y_vector *= -1
    y = 1

  pygame.display.flip()