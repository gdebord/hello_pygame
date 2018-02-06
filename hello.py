import pygame, sys, time

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
#pygame.draw.polygon(DISPLAYSURF, GREEN, ((196,30),(341,136),(286,307),(106,307),(50,136)))

x = 5
diff = 5
x_vector = 1
y_vector = 1

while True: # main game loop    

  for event in pygame.event.get():

    DISPLAYSURF.fill(WHITE)  

    if event.type == QUIT:

      pygame.quit()

      sys.exit()

    else:

      pygame.draw.polygon(DISPLAYSURF, GREEN, ((196+x_vector, 30+y_vector),(341+x_vector, 136+y_vector),(286+x_vector,307+y_vector),(106+x_vector,307+y_vector),(50+x_vector,136+y_vector)))

      if x_vector < 50:
        x_vector += 5
        y_vector += 5

    pygame.display.update()