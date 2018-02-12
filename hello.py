import pygame, sys, time, math, random

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 800))

pygame.display.set_caption('Hello World!')

# setup colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)

x = 200
y = 200
x_vector = random.randrange(-15,6)
y_vector = random.randrange(-5,6)
done = False

while not done: # main game loop  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  DISPLAYSURF.fill(WHITE)

  x = math.floor(x + x_vector)
  y = math.floor(y + y_vector)
  pygame.draw.circle(DISPLAYSURF, GREEN, (x , y), 10, 0)

  if (x > 800):
    x_vector *= -1
    x = 799
  elif (y > 800):
    y_vector *= -1
    y = 799
  elif (x < 0):
    x_vector *= -1
    x = 1
  elif (y < 0):
    y_vector *= -1
    y = 1

  pygame.display.flip()