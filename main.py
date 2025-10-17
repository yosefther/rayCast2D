import sys
import pygame
from map import Map
from settings import *
screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HIGHT))
map = Map()
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    

    screen.fill(0)
    map.render(screen)
    pygame.display.update()
