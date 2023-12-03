import pygame as pg
from pygame.math import Vector2
class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoint = waypoints
        self.position = Vector2(self.waypoint[0])
        self.target_waypoint = 1
        self.speed = 2
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        self.move()

    #create movement method
    def move(self):
        #create a position waypoint to head to.
        self.target = Vector2(self.waypoint[self.target_waypoint])
        self.movement = self.target - self.position
        #here we are using the normalize method in the Sprite class to convert our position in
        # the x direction and y direction to get our direction in pixels using trig
        self.position += self.movement.normalize() * self.speed
        self.rect.center = self.position