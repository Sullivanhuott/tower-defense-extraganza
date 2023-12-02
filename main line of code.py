import pygame as pg
from enemy import Enemy
import constants as c

# initializing
pg.init()

#clock creation
clock = pg.time.Clock()

# create screen dimensions and screen name
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("defence of Huottalonia")

#Enemy images
ghost_image = pg.image.load('assets/dungeon/Tiles/ghost.png').convert_alpha()

#create ghost group
enemy_group = pg.sprite.Group()


ghost = Enemy((200,300), ghost_image)
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

    #update groups
    enemy_group.update()

    #drawing part of loop
    enemy_group.draw(screen)

    #event_handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    #update display
    pg.display.flip()

pg.quit()
