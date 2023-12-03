import pygame as pg

class Level():
    def __init__(self, level_image):
        self.image = level_image

    def draw(self, surface):
        surface.blit(self.image, (0, 0))