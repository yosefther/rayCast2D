# pyright: ignore[reportMissingImports]
import pygame
from settings import *
from ray import Ray

class Raycaster:
    def __init__(self, player):
        self. rays=[]
        self.player = player 

    def castAllRays(self):
        ...

    def render(self , secreen):
        for ray in self.rays:
            ray.render(secreen   )
        
        

