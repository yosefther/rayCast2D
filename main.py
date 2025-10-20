import sys
import pygame
from map import Map
from player import Player
from settings import *
screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
map = Map()
player = Player()
clock = pygame.time.Clock()
while True :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    player.update()

    screen.fill((0,0,0))
    map.map_render(screen)
    player.player_render(screen)
    
    pygame.display.update()
