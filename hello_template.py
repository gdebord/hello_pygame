import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Hello World!')

# define some variables to store colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# define some variables to draw with
x = 200
y = 200

# draw a white screen
DISPLAY.fill(BLACK)

# main game loop (infinite loop)
while True:  

  # draw a green circle at the given x,y coordinates
  pygame.draw.circle(DISPLAY, BLUE, (x , y), 10, 0)

  # if the user clicks to close the window, the program exits
  for event in pygame.event.get():

    if event.type == QUIT:

      pygame.quit()

      sys.exit()

    # update the screen
    pygame.display.update()