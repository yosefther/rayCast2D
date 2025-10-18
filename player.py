import pygame
import math
from settings import *

class Player:
    def __init__(self):
        self.x =WINDOW_WIDTH // 2 + 30
        self.y = WINDOW_HIGHT // 2
        self.radius = 10

    def playr_render(self, screen):
        pygame.draw.circle(screen ,(255,0,0), (self.x, self.y) , self.radius)
