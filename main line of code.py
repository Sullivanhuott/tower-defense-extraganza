import sys
import pygame
import random
import time

pygame.init()

print('\nRunning the main line of code.py.')
print('---------------------------------')


#screen dimensions here
screen_wid = 800
screen_hgt = 600

#drawing template for town

screen = pygame.display.set_mode((screen_wid, screen_hgt))
pygame.display.set_caption('Lilheims Town')

def Lilheims(surface):
    grass =pygame.image.load('../assets/town/Tiles/tile_0000.png').convert()

    ''' how to make black pixels transparent, ex: grass.set_colorkey((0,0,0))'''
    # make a flat grass back ground
    for x in range(0, surface.get_width(), grass.get_width()):
        for y in range(0, surface.get_height(), grass.get_height()):
            surface.blit(grass, (x,y))
background = screen.copy()
Lilheims(background)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    pygame.display.flip()

print('\n--------------------')
print('End of line.')
pygame.quit()
sys.exit()