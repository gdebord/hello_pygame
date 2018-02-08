import pygame, sys, time, math, random

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400))

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
x_vector = random.randrange(-5,6)
y_vector = random.randrange(-5,6)

while True: # main game loop  

  DISPLAYSURF.fill(WHITE)
  pygame.draw.circle(DISPLAYSURF, GREEN, (x,y), 10, 0)  

  for event in pygame.event.get():

    DISPLAYSURF.fill(WHITE)

    if event.type == QUIT:

      pygame.quit()

      sys.exit()

    else:

      x = math.floor(x + x_vector)
      y = math.floor(y + y_vector)
      pygame.draw.circle(DISPLAYSURF, GREEN, (x , y), 10, 0)

      if (x > 400):
        x_vector *= -1
        x = 399
      elif (y > 400):
        y_vector *= -1
        y = 399
      elif (x < 0):
        x_vector *= -1
        x = 1
      elif (y < 0):
        y_vector *= -1
        y = 1

    pygame.display.update()