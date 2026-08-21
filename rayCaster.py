# pyright: ignore[reportMissingImports]
import pygame
from settings import *
from ray import Ray

class Raycaster:
    def __init__(self , player):
        self.rays=[]
        self.player = player 
    def RayCaster(self):
        rayAngle = self.player.rotationAngle - FIELD_OF_VIEW / 2
        # rayAngle = (self.player.rotationAngle - 30)

        for i in range(NUM_RAYS):
            ray = Ray(rayAngle , self.player)
            ray.cast()
            self.rays.append(ray)
            rayAngle += FIELD_OF_VIEW / NUM_RAYS

    def render(self,screen):
        for ray in self.rays :
            ray.render(screen)
