import pygame as pg
from enemy import Enemy
from allies import Ally
from button import Button
from levels import Level
import constants as c
from PIL import Image
import math

# initializing
pg.init()

#clock creation
clock = pg.time.Clock()

#game variables
placing_ally = False

# create screen dimensions and screen name
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
pg.display.set_caption("Defence of Huottalonia")

#loading in the map image I created
Huottalonia_image = pg.image.load('assets/huottalonia_gate_map.png').convert_alpha()

#Ally images
grunt_image = pg.image.load('assets/dungeon/Tiles/grunt.png').convert_alpha()

#Enemy images
ghost_image = pg.image.load('assets/dungeon/Tiles/ghost.png').convert_alpha()

#buttons
buy_ally_image = pg.image.load("assets/dungeon/Tiles/scaledgrunt.png").convert_alpha()
cancel_ally_image = pg.image.load("assets/bettercrossedswords_new.png").convert_alpha()
ally_button = Button(c.SCREEN_WIDTH + 75, 60, buy_ally_image, True)
cancel_button = Button(c.SCREEN_WIDTH+ 200, 60, cancel_ally_image, True)


#finding the color of my tower
image_path = "assets/huottalonia_gate_map.png"
image = Image.open(image_path)
'''pixel_x = 120
pixel_y = 377            #this was me finding the color of the tower lol.
pixel_color = image.getpixel((pixel_x, pixel_y))
print(pixel_color)'''
def create_ally(mouse_position):
    mouse_tile_x = mouse_position[0] // c.TILE_SIZE
    mouse_tile_y = mouse_position[1] // c.TILE_SIZE
    pixel_color = image.getpixel((mouse_position[0],mouse_position[1]))
    #check for tower
    if pixel_color == (192,203,220,255):
        #check for preexisting ally
        freespace = True
        for Grunt in ally_group:
            if (mouse_tile_x,mouse_tile_y) == (Grunt.tile_x, Grunt.tile_y):
                freespace = False
        if freespace == True:
            new_Grunt = Ally(grunt_image, mouse_tile_x, mouse_tile_y)
            ally_group.add(new_Grunt)
    else:
        pass

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
#####################################################################################################################
#main game loop
run = True
while run:
    #FPS set to 60
    clock.tick(c.FPS)
    ###################
    #UPDATING SECTIONS
    ###################
    enemy_group.update()

    ###################
    #drawing section
    ###################

    #clear screen between each loop
    screen.fill("grey100")

    #draw level
    Huottalonia.draw(screen)

    #drawing part of loop
    enemy_group.draw(screen)
    ally_group.draw(screen)

    #drawing buttons
    if ally_button.draw(screen):
        placing_ally = True
    #shwo cancel button if placing allies.
    if placing_ally == True:
        #show ally on cursor but in game screen only.
        cursor_rect = grunt_image.get_rect()
        cursor_position = pg.mouse.get_pos()
        cursor_rect.center = cursor_position
        if cursor_position[0] <= c.SCREEN_WIDTH:
            screen.blit(grunt_image, cursor_rect)
        if cancel_button.draw(screen):
            placing_ally = False


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
                #only place allies if you click the button
                if placing_ally == True:
                    create_ally(mouse_position)

    #update display
    pg.display.flip()

pg.quit()
