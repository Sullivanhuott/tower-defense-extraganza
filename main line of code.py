import pygame as pg
import constants as c

# initializing
pg.init()


#clock creation
clock = pg.time.Clock()



# create screen dimensions and screen name
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("defence of Huottalonia")

#title game loop

#main game loop
run = True
while run:
    clock.tick(c.FPS)
    #event_handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()
