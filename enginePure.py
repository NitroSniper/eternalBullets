from math import sin, cos, radians, sqrt, atan2, degrees, pi
from time import perf_counter
from typing import Tuple
import pygame
import random
from pygame import gfxdraw
class ModuleDependency(object):
    try:
        import numpy
        isNumpyHere = True
    except ModuleNotFoundError:
        isNumpyHere = False
    try:
        import numba
        isNumbaHere = True
    except ModuleNotFoundError:
        isNumbaHere = False
    allModule = all((isNumbaHere, isNumpyHere))
    

def cartesianToPolar(array):
    output = []
    for x, y in array:
        r = sqrt(x**2 + y**2)
        theta = degrees(atan2(y, x))
        output.append((r, theta))
    return output


def polarToCartesian(rAndBasetheta, angle):
    #note theta is in degrees and not radians
    output = []
    for i, rtheta in enumerate(rAndBasetheta):
        output.append((round(cos(radians(rtheta[1]+angle))*rtheta[0]), 
                      round(sin(radians(rtheta[1]+angle))*rtheta[0])))
    return output

def regularShape(radius, nSide):
    #side = side length
    if nSide < 3: nSide = 3 
    interval = 2*pi/nSide
    return [(cos(i*interval-pi/4)*radius, sin(i*interval-pi/4)*radius) for i in range(nSide)]

#https://krazydad.com/tutorials/makecolors.php
#https://www.instructables.com/How-to-Make-Proper-Rainbow-and-Random-Colors-With-/

class StaticColor(object):
    def __init__(self, color):
        self.color = color
    def returnColor(self, colorMultiplier):
        return self.color
DEFAULT_COLOR = StaticColor(255)


class ColorObject(object):
    def __init__(self, color, lowerBound, upperBound, overflowFunc):
        #what is self.color
        self.baseColor = color
        self.limits = (lowerBound, upperBound)
        self.difference = upperBound - lowerBound
        if overflowFunc != ColorObject.modColor:
            self.waveLength = 2*pi/self.difference
            self.centre = (lowerBound+upperBound)/2
            self.baseColor = color/360 * self.difference
        self.overflow = overflowFunc
        self.reverse = False
    def returnColor(self, colorMultiplier):
        return self.overflow(self, self.baseColor + self.difference*colorMultiplier)#

    def modColor(self, color):
        if self.reverse:
            self.limits[1] - color % self.difference
        return self.limits[0] + color % self.difference

    def sinColor(self, color):
        return self.centre + sin(color*self.waveLength)*self.difference

    def posSinColor(self, color):
        return self.limits[0]+max(0, sin(color*self.waveLength)*self.difference)

class ColorOverview(object):
    def __init__(self, r=DEFAULT_COLOR, g=DEFAULT_COLOR, b=DEFAULT_COLOR, alpha=DEFAULT_COLOR):
        # color are given a lower and upper
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = alpha
        self.start = perf_counter()
    def update(self, dt):
        pass
    def giveColorArgs(self):
        ColorMultiplier = (perf_counter() - self.start)/1
        return (self.red.returnColor(ColorMultiplier),
                self.green.returnColor(ColorMultiplier),
                self.blue.returnColor(ColorMultiplier),
                self.alpha.returnColor(ColorMultiplier))
def foo():
    return ColorOverview(
    r=ColorObject(0, 128, 255, ColorObject.posSinColor),
    g=ColorObject(120, 128, 255, ColorObject.posSinColor),
    b=ColorObject(240, 128, 255, ColorObject.posSinColor)
    )


class PolygonClass(object):
    def __init__(self, vertices, color=None, rotationSpeed=1):
        self.vertices = cartesianToPolar(vertices)
        self.rotationSpeed = rotationSpeed
        self.color = foo()

    def giveGFXArgs(self, rotation):
        return (polarToCartesian(self.vertices, rotation*self.rotationSpeed), self.color.giveColorArgs())
    def __str__(self):
        return f'{len(self.vertices)} shape polygon with {str(self.rotation)[:5]} rotation'


class PolygonOverview(object):
    def __init__(self, polygons):
        self.polygons = polygons
        self.internalRotation = 0
        self.internalRotationIncrease = 1
        self.polygonSize = max(r for i in self.polygons for r, _ in i.vertices)
    def update(self, dt, externalRotation=0, externalRotationIncrease=0):
        self.internalRotation += (externalRotationIncrease + self.internalRotationIncrease)*dt
        rotation = self.internalRotation + externalRotation
        self.image = drawGFXShapes([polygon.giveGFXArgs(rotation) for polygon in self.polygons], self.polygonSize)


def drawGFXShapes(arrayOfPolygonInfo, polygonSize):
    surf = pygame.Surface((2*(polygonSize), 2*(polygonSize)), pygame.SRCALPHA)
    offset = None
    for vertices, color in arrayOfPolygonInfo:
        offsetted = [(v[0] + polygonSize, v[1] + polygonSize) for v in vertices]
        #print (offsetted, end='\r')
        gfxdraw.aapolygon(surf, offsetted, color)
        gfxdraw.filled_polygon(surf, offsetted, color)
    return surf



