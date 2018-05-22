import pygame, sys, time, math, random, pygame.freetype

from pygame.locals import *

pygame.init()
pygame.freetype.init()

#font_name = pygame.freetype.get_default_font

def draw_text(surf, text, size, x, y):
    #font = pygame.font.Font(font_name, size)
    font = pygame.freetype.SysFont('Arial', 50)
    text_surface = pygame.freetype.Font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

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

x2 = 100 # coordinates for rectangle
y2 = 100

a = 10 # for moving rectangle

score1 = 0
score2 = 3

done = False

while not done: # main game loop  

  draw_text(DISPLAYSURF, "007", 50, 250, 150)

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

  DISPLAYSURF.fill(BLACK)

  pygame.draw.circle(DISPLAYSURF, GREEN, (x , y), 10, 0) # draw circle

  pygame.draw.rect(DISPLAYSURF, BLUE, (x2, y2, 20, 100), 0) # draw rectangle

  # UPDATE THE SCREEN
  pygame.display.flip()