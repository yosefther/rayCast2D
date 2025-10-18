import pygame
from settings import *
class Map:
    def __init__(self):
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1],
            [1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1],
            [1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1],
            [1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
            [1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1],
            [1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1],
            [1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1],
            [1,0,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1],
            [1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1],
            [1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

    def map_render(self , screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                TILE_X = j * TILESIZE  # EXAPLE : TILESIZE * index_j_0 = 0 // 63 * index_j_1 = 64 
                TILE_Y = i * TILESIZE   
                if self.grid[i][j] == 0:
                    pygame.draw.rect(screen , (255, 255, 255) , (TILE_X ,  TILE_Y, TILESIZE -1,TILESIZE -1)) 
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(screen , (105,105,105) , (TILE_X ,  TILE_Y, TILESIZE -1 ,TILESIZE -1  )) 
        
    def has_wall_at(self ,x ,y,*args):
        return self.grid[int(y//TILESIZE)][int(x//TILESIZE)] == 1