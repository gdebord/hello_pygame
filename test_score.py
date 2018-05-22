import pygame, sys, time, math, random, pygame.freetype

from pygame.locals import *

pygame.init()
pygame.freetype.init()

# define a funtion to draw text on display surface
def draw_text(surf, text, size, x, y):
    font = pygame.freetype.Font(None, 20)
    text_surface = font.render_to(surf, (x,y), text, WHITE, size=size)

XSCREEN = 500
YSCREEN = 500

DISPLAYSURF = pygame.display.set_mode((XSCREEN, YSCREEN))

pygame.display.set_caption('PONG')

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

x2 = 10 # coordinates for rectangle
y2 = 100

a = 10 # for moving rectangle

score1 = 0 # left player score
score2 = 3 # right player score

done = False

while not done: # main game loop  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN: # looks at which key is pushed
    	if event.key == pygame.K_w: # up
    		y2 -= a
    	if event.key == pygame.K_a: # left
    		x2 -= a
    	if event.key == pygame.K_s: # down
    		y2 += a
    	if event.key == pygame.K_d: # right
    		x2 += a

  DISPLAYSURF.fill(BLACK) # fill black background

  draw_text(DISPLAYSURF, str(x2), 80, 125, 10) # draw left score
  draw_text(DISPLAYSURF, str(y2), 80, 325, 10) # draw right score

  pygame.draw.circle(DISPLAYSURF, WHITE, (x , y), 10, 0) # draw circle

  pygame.draw.rect(DISPLAYSURF, WHITE, (x2, y2, 15, 60), 0) # draw rectangle

  # UPDATE THE SCREEN
  pygame.display.flip()