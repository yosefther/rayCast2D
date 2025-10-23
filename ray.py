import math , pygame 

def normalizedAngle(angle):
    angle = angle % (2 *math.pi)
    if (angle < 0) :
        angle = (2* math.pi) + angle
    return angle


class Ray:
    def __init__(self, angle , player):
        self.player = player
        self.rayAngle = normalizedAngle(angle)

    def cast(self):
        ...

    def render(self , secreen):
        pygame.draw.line(secreen , (255,0,0) ,
        (self.player.x , self.player.y ) ,
        (self.player.x + math.cos(self.rayAngle)*50 ,
        self.player.y  + math.sin(self.rayAngle)*50  ) )
