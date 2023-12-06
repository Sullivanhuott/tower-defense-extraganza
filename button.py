import pygame as pg
from PIL import Image

org_grunt_image = Image.open("assets/dungeon/Tiles/grunt.png")
scale_factor = 3
new_width = int(org_grunt_image.width * scale_factor)
new_height = int(org_grunt_image.height * scale_factor)
scaled_grunt_image = org_grunt_image.resize((new_width, new_height))
scaled_grunt_image.save("assets/dungeon/Tiles/scaledgrunt.png")

org_sword_image = Image.open("assets/bettercrossedswords.png")
scale_factor = .10
new_width = int(org_sword_image.width * scale_factor)
new_height = int(org_sword_image.height * scale_factor)
scaled_grunt_image = org_sword_image.resize((new_width, new_height))
scaled_grunt_image.save("assets/bettercrossedswords_new.png")

org_anvil_image = Image.open("assets/dungeon/Tiles/anvil.png")
scale_factor = 3
new_width = int(org_anvil_image.width * scale_factor)
new_height = int(org_anvil_image.height * scale_factor)
scaled_grunt_image = org_anvil_image.resize((new_width, new_height))
scaled_grunt_image.save("assets/dungeon/Tiles/scaledanvil.png")

class Button():
    def __init__(self, x, y, image, single_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.single_click = single_click

    def draw(self, surface):
        action = False
        #mouse position
        position = pg.mouse.get_pos()
        #check mouse over and pressing
        if self.rect.collidepoint(position):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                #differentiating between single click and click and hold
                if self.single_click:
                    self.clicked = True
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked == False
        #draw button
        surface.blit(self.image, self.rect)

        return action