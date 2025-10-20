import pygame
import math
from settings import *

class Player:
    def __init__(self):
        self.x =WINDOW_WIDTH // 2 + 30
        self.y = WINDOW_HEIGHT // 2
        self.turnDirection = 0 
        self.walkDirection = 0
        self.moveSpeed = 3.5
        self.radius = 10
        self.rotationSpeed = 0.05

        self.rotationAngle = math.pi / 10

    def update (self):

        keys = pygame.key.get_pressed()
        self.turnDirection = 0 
        self.walkDirection = 0

        # Rotation controls
        if keys[pygame.K_RIGHT]:
            self.turnDirection = 1 
        if keys[pygame.K_LEFT]:
            self.turnDirection = -1
            
        # Movement controls  
        if keys[pygame.K_UP]:
            self.walkDirection = 1  
        if keys[pygame.K_DOWN]:
            self.walkDirection = -1  

        moveStep = self.walkDirection * self.moveSpeed
        self.rotationAngle += self.turnDirection * self.rotationSpeed
        self.x += math.cos(self.rotationAngle) * moveStep
        self.y += math.sin(self.rotationAngle) * moveStep




    def player_render(self, screen):
        pygame.draw.circle(screen ,(255,0,0), (self.x, self.y) , self.radius)
        pygame.draw.line(screen,(255,0,0), (self.x , self.y) , (self.x+math.cos(self.rotationAngle)*100 , self.y+ math.sin(self.rotationAngle)*100) )
        