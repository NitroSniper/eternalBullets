import pygame
from Composition import PolygonClass
class PlayerObject(object):
    def __init__(self, keys):
        '''DOCSTRING'''
        self.keys = keys #<show> Player Control Key
        self.movements = {
            'UP' : False,
            'DOWN' : False,
            'LEFT' : False,
            'RIGHT' : False
        }
        self.x = 200 #<show> Player x coordinate
        self.y = 300 #<show> Player y coordinate
        self.image = pygame.surface.Surface((30, 30)) #<show> Player image
        self.image.fill((0,0,255))
        self.speed = 3 #<show> Player movement speed
        self.polygons = [PolygonClass(((0,0), (0, 50), (50, 0), (50, 50))) for i in range(1000)]
    def update(self, dt):
        if self.movements['UP']: #<show> if movement 'up' is True
            self.y -= self.speed*dt #<show> Player moves upwards
        if self.movements['DOWN']: #<show> if movement 'down' is True
            self.y += self.speed*dt #<show> Player moves downwards
        if self.movements['LEFT']: #<show> if movement 'left' is True
            self.x += self.speed*dt #<show> Player moves to the left
        if self.movements['RIGHT']: #<show> if movement 'right' is True
            self.x -= self.speed*dt #<show> Player moves to the right
        for polygon in self.polygons:
            polygon.update(dt)