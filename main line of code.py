import pygame as pg
from enemy import Enemy
from allies import Ally
from levels import Level
import constants as c
import math

# initializing
pg.init()

#clock creation
clock = pg.time.Clock()

# create screen dimensions and screen name
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Defence of Huottalonia")

#loading in the map image I created
Huottalonia_image = pg.image.load('assets/huottalonia_gate_map.png').convert_alpha()

#Ally images
grunt_image = pg.image.load('assets/dungeon/Tiles/grunt.png').convert_alpha()

#Enemy images
ghost_image = pg.image.load('assets/dungeon/Tiles/ghost.png').convert_alpha()

def create_ally(mouse_position):
    mouse_tile_x = mouse_position[0] // c.TILE_SIZE
    mouse_tile_y = mouse_position[1] // c.TILE_SIZE
    Grunt = Ally(grunt_image, mouse_tile_x, mouse_tile_y)
    ally_group.add(Grunt)

#create level
Huottalonia = Level(Huottalonia_image)
#create enemy group
enemy_group = pg.sprite.Group()
#create ally group
ally_group = pg.sprite.Group()
waypoints = [
    (72,496),
    (72,328),
    (376,328),
    (376,169),
    (231,169),
    (231,0)
]

ghost = Enemy(waypoints, ghost_image)
enemy_group.add(ghost)

print(ghost)


#title game loop

#main game loop
run = True
while run:
    #FPS set to 60
    clock.tick(c.FPS)

    #clear screen between each loop
    screen.fill("grey100")

    #draw level
    Huottalonia.draw(screen)

    #update groups
    enemy_group.update()

    #drawing part of loop
    enemy_group.draw(screen)
    ally_group.draw(screen)

    #event_handler
    for event in pg.event.get():
        #quit function
        if event.type == pg.QUIT:
            run = False
        #placing ally mouse event
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pg.mouse.get_pos()
            # check if mouse is on the map by limiting the placement to below the x distance of the
            # game width and the map height
            if mouse_position[0] < c.SCREEN_WIDTH and mouse_position[1] < c.SCREEN_HEIGHT:
                create_ally(mouse_position)

    #update display
    pg.display.flip()

pg.quit()
