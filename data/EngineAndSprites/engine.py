from math import sin, cos, radians, sqrt, atan2, degrees
import numpy as np
import numba as nb
import pygame
from pygame import gfxdraw


def cartesianToPolar(array):
    output = np.zeros_like(array)
    for i, xy in enumerate(array):
        x = xy[0]
        y = xy[1] 
        output[i][0] = sqrt(x**2 + y**2)
        output[i][1] = degrees(atan2(y, x))
    return output


@nb.njit()
def polarToCartesian(rAndBasetheta, angle):
    #note theta is in degrees and not radians
    output = np.zeros_like(rAndBasetheta)
    for i, rtheta in enumerate(rAndBasetheta):
        output[i][0] = cos(radians(rtheta[1]+angle))*rtheta[0]
        output[i][1] = sin(radians(rtheta[1]+angle))*rtheta[0]
    return output

class PolygonOverview(object):
    def __init__(self, polygons):
        self.polygons = np.array(polygons)
        self.internalRotation = 0
        self.internalRotationIncrease = 1
        self.polygonSize = max(r for i in self.polygons for r, _ in i.vertices)

    def update(self, dt, externalRotation=0, externalRotationIncrease=0):
        self.internalRotation += (externalRotationIncrease + self.internalRotationIncrease)*dt
        rotation = self.internalRotation + externalRotation
        self.image = drawGFXShapes([polygon.giveGFXArgs(rotation) for polygon in self.polygons], self.polygonSize)
    
class PolygonClass(object):
    def __init__(self, vertices):
        self.vertices = np.array(cartesianToPolar(vertices))
        self.rotationSpeed = 1
        #This could be made as an object
        self.color = (255, 255, 255)
        self.alpha = 255
    
    def giveGFXArgs(self, rotation):
        return polarToCartesian(self.vertices, rotation), self.color, self.alpha
    
@nb.vectorize()
def arrayOffset(array, offset):
    return array + offset

def drawGFXShapes(arrayOfPolygonInfo, polygonSize):
    surf = pygame.Surface((2*(polygonSize), 2*(polygonSize)), pygame.SRCALPHA)
    for vertices, color, alpha in arrayOfPolygonInfo:
        offsetted = arrayOffset(vertices, polygonSize)
        gfxdraw.aapolygon(surf, offsetted, color + (alpha,))
        gfxdraw.filled_polygon(surf, offsetted, color + (alpha,))
    return surf