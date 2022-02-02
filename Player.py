import pygame
from enginePure import ModuleDependency, regularShape
from math import sqrt
print (ModuleDependency.allModule)
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from enginePure import PolygonOverview, PolygonClass



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
        #self.polygon = PolygonOverview((PolygonClass(((40, 40), (40, -40), (-40, -40), (-40, 40))), PolygonClass(((20, 20), (20, -20), (-20, -20), (-20, 20))),))
        self.polygon = PolygonOverview((
            PolygonClass(regularShape(32*sqrt(2), 4)),
            ))
        print (self.polygon.polygons[0].vertices)
    def update(self, dt):
        if self.movements['UP']: #<show> if movement 'up' is True
            self.y -= self.speed*dt #<show> Player moves upwards
        if self.movements['DOWN']: #<show> if movement 'down' is True
            self.y += self.speed*dt #<show> Player moves downwards
        if self.movements['LEFT']: #<show> if movement 'left' is True
            self.x += self.speed*dt #<show> Player moves to the left
        if self.movements['RIGHT']: #<show> if movement 'right' is True
            self.x -= self.speed*dt #<show> Player moves to the right
        self.polygon.update(dt)
        self.image = self.polygon.image
