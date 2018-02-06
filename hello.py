import pygame, sys

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
pygame.draw.polygon(DISPLAYSURF, GREEN, ((196,30),(341,136),(286,307),(106,307),(50,136)))



while True: # main game loop

  for event in pygame.event.get():

    if event.type == QUIT:

      pygame.quit()

      sys.exit()

    pygame.display.update()