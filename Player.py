from __future__ import annotations
from typing import Union


import pygame
from time import perf_counter
from random import randint
from enginePure import ModuleDependency, regularShape, Overview, RAINBOW, EMPTY_COLOR, FULL_COLOR
from Trails import TrailObject
from math import sqrt, atan2, degrees



print (ModuleDependency.allModule)
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from enginePure import PolygonOverview, PolygonClass, ColorOverview, DynamicColor, StaticPoint, StaticColor, LinearPoint, RGBtoStaticColor


class PlayerObject(object):
    def __init__(self, keys):
        '''DOCSTRING'''
        self.keys = keys #<show> Player Control Key
        self.movements = {
            'UP' : False,
            'DOWN' : False,
            'LEFT' : False,
            'RIGHT' : False
        } #<show> these are holding which direction the player will be moving
        self.size = 40 #<show> player size in the game
        self.x = 960-self.size/2 #<show> Player x coordinate
        self.y = 540-self.size/2 #<show> Player y coordinate
        self.speed = 3 #<show> Player movement speed   
        self.polygon = PolygonOverview((PolygonClass(((40, 40), (40, -40), (-40, -40), (-40, 40))), PolygonClass(((20, 20), (20, -20), (-20, -20), (-20, 20))),))
        polygon1 = {
            'vertices': regularShape(self.size/2, 4),
            'color': {
                'r':DynamicColor(0, 2, 0, DynamicColor.sinColor),
                'g':DynamicColor(0, 97, 247, DynamicColor.sinColor),
                'b':DynamicColor(0, 199, 255, DynamicColor.sinColor),
                'player' : True
                },
            'rotationSpeed': 1,
                    } #<show> polygon info argument for 1 of the polygon
        polygons = {
            'polygons' : (polygon1,),
            'rotation': 45,
            'rotationIncrease' : 0
        } #<show> complete polygon argument
        self.polygon = PolygonOverview(**polygons) #<show> polygon attribute to the player
        # self.polygon = PolygonOverview((PolygonClass(regularShape(120, 3), ColorOverview()), PolygonClass(regularShape(60, 3), ColorOverview(alpha=StaticColor(0))), PolygonClass(regularShape(20, 4), ColorOverview(r=FULL_COLOR, g=EMPTY_COLOR, b=EMPTY_COLOR), rotationSpeed=-1)))
        self.polygon.update(0)
        self.image = self.polygon.image
        
        self.trailSize = 8 #<show> trail size

        self.trailStart = perf_counter() #<show> last time since trail is created
        self.lastInvinciblity = perf_counter() #<show> last time since player was invincible
    def update(self, dt, externalRotation=0) -> None:
        self.moving = any(self.movements.values()) #<show> is Player moving? 
        direction = [0, 0] #<show> holds the offset of 
        if self.moving: #<show> if the player is moving
            if self.movements['UP']: #<show> if movement 'up' is True
                direction[1] -= self.speed*dt #<show> Player moves upwards
            if self.movements['DOWN']: #<show> if movement 'down' is True
                direction[1] += self.speed*dt #<show> Player moves downwards
            if self.movements['LEFT']: #<show> if movement 'left' is True
                direction[0] += self.speed*dt #<show> Player moves to the left
            if self.movements['RIGHT']: #<show> if movement 'right' is True
                direction[0] -= self.speed*dt #<show> Player moves to the right
        self.x += direction[0]; self.y += direction[1] #<show> add direction onto player current position
        direction = degrees(atan2(-direction[1], -direction[0])) #<show> find the angle the player is going to
        self.polygon.update(dt, externalRotation=direction+externalRotation) #<show> update player polygon image
        self.image = self.polygon.image #<show> set polygon image as image
        
        if self.moving and 0.1 < perf_counter() - self.trailStart: #<show> if moving and you can spawn another trail
            self.trailStart = perf_counter() #<show> set trail spawn last as now
            self.trailSize = randint(4, 12)
            currentColor = self.polygon.polygons[0].color.giveColorArgs(alpha=False) #<show> get the current color of the player
            polygon = {
                'vertices': regularShape(self.trailSize, 4),
                'color': {
                    'r': StaticColor(currentColor[0]),
                    'g': StaticColor(currentColor[1]),
                    'b': StaticColor(currentColor[2]),
                    'alpha': DynamicColor(0, 255, 0, DynamicColor.modColor, reverse=False),
                    'trail' : True
                    }
                }  #<show> trail polygon argument
            TrailObject(LinearPoint(self.x + (self.size - self.trailSize)/2, self.y + (self.size - self.trailSize)/2, direction+randint(-10, 10), 5),
                        PolygonOverview((polygon,), self.polygon.internalRotation, randint(1, 5)), 1) #<show> creating trail

        if 1 < perf_counter() - self.lastInvinciblity:  #<show> if player is not invincible
            rect = self.get_rect() #<show> get player rect
            for bullet in Overview.BULLETS: #<show> for all bullets
                bulletRect = bullet.get_rect() #<show> get bullet rect
                if rect.colliderect(bulletRect): #<show> if bulletRect is colliding with player rect
                    self.lastInvinciblity = perf_counter() #<show> set last invincibility time as now
                    self.polygon.polygons[0].color.fade.fadeFrom(ColorOverview(**RGBtoStaticColor(255, 0, 0)), duration=0.5, startingPercent=1)
                    #<show> make the background flash red
                    break

    
    
    def get_rect(self) -> pygame.Rect:
        return self.image.get_rect(topleft=(self.x, self.y))  #<show> return player rect

            
#crazy frog axel
