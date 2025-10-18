import sys
import pygame
from map import Map
from player import Player
from settings import *
screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HIGHT))
map = Map()
player = Player()
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    screen.fill((0,0,0))
    map.map_render(screen)
    player.playr_render(screen)

    pygame.display.update()
