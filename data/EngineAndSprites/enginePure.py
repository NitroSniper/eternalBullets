# mahie's code is not elite, i was gonna say it is but i dont like him :D

from operator import itemgetter
from random import random
from math import sin, cos, radians, sqrt, atan2, degrees, pi, ceil, acos
from pickle import GLOBAL
from time import perf_counter
import pygame
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



class DecayingNumber(object):
    def __init__(self):
        self.currentNumber = 0
        self.start = perf_counter()
        self.duration = 0
    def update(self):
        elapsed = perf_counter() - self.start
        if not self.duration:
            pass
        elif self.duration > elapsed:  # <show> means it is still going
            self.currentNumber = self.number*(1-elapsed/self.duration)
        else:
            self.currentNumber = 0
            self.duration = 0
    
    def setDecayingValue(self, number, duration):
        self.duration = duration
        self.number = number
        self.start = perf_counter()


class CameraObject(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

        self.shake = (DecayingNumber(), DecayingNumber())

    def update(self, dt):
        
        for shakeAxis in self.shake:
            shakeAxis.update()

        self.x += self.dx*dt
        self.y += self.dy*dt

    def CameraOffset(self, x, y):
        return (x - (self.x + self.shake[0].currentNumber),
                y - (self.y + self.shake[1].currentNumber))

    # def Shaking(self, duration, magnitude):
    #     self.shakeDuration = duration
    #     self.shakeStart = perf_counter()
    #     self.shakeOffset = ((random()-0.5)*self.shakeMagnitude,
    #                         (random()-0.5)*self.shakeMagnitude)

    def blinking(self, duration, x=0, y=0):
        for shakeAxis, number in zip(self.shake, (x,y)):
            if number:
                shakeAxis.setDecayingValue(number, duration)
        # self.shakeDuration = duration
        # self.shakeStart = perf_counter()
        # self.shakeOffset = (x, y)

    def easing(self, percent):  # <show> find the ratio between 2 different points
        # 1 means more color 2, which is the newer color and 0 is more color 1
        return (self.shakeOffset[0]*(1-percent),
                self.shakeOffset[1]*(1-percent))  # <show> gets the ratio between the 2 different points

    def __add__(self, position):
        '''
        adds the camera position to the position given.
        '''
        return (position[0] - (self.x + self.shake[0].currentNumber),
                position[1] - (self.y + self.shake[1].currentNumber))


class Fading(object):
    def __init__(self, parent=None):
        self.fadeColor = None  # <show> set fadeColor as color given
        self.fadeDuration = None  # <show> set fadeDuration as duration given
        self.fadeStart = perf_counter()  # <show> set fade start as current time
        # <show> set startingPercent for ratio color as percent given
        self.startingPercent = None
        # <show> find out the alpha Mutliplier so it still goes the same speed
        self.alphaMultiplier = None
        self.priority = None  # <show> give the fading a priority which it has
        self.fromfunc = None
        if parent is None:
            self.parent = (self,)
        else:
            self.parent = (self,) + parent

    def fading(self, r, g, b, alpha):  # <show> if fading is possible
        col = (r, g, b, alpha)
        for obj in self.parent:
            elapsed = perf_counter() - obj.fadeStart
            if not obj.fadeDuration:  # if fadeDuration is 0 then return
                continue  # <show> return normal color
            # <show> show the elapsed amount of time since it was created
            # <show> if the fading is still happening
            #print (elapsed/(obj.alphaMultiplier))
            elif obj.endingPercent + elapsed/(obj.alphaMultiplier) < obj.startingPercent:
                # <show> return the ratio between the two colors
                col = obj.ratioColor(
                    col, elapsed/obj.alphaMultiplier, obj.fromfunc)
            else:  # <show> if not fading meaning it has just finished
                obj.fadeDuration = 0  # <show> set to 0
                obj.priority = None  # <show> it has no priority
                continue
        return col

    # <show> if fading from a color
    def fadeFrom(self, color, duration, startingPercent=1, endingPercent=0):
        self.fadeColor = color  # <show> set fadeColor as color given
        self.fadeDuration = duration  # <show> set fadeDuration as duration given
        self.fadeStart = perf_counter()  # <show> set fade start as current time
        # <show> set startingPercent for ratio color as percent given
        self.startingPercent = startingPercent
        self.endingPercent = endingPercent
        # <show> find out the alpha Mutliplier so it still goes the same speed
        self.alphaMultiplier = duration/(startingPercent - endingPercent)
        self.fromfunc = True

    def fadeTo(self, color, duration, startingPercent=1, endingPercent=0):
        self.fadeColor = color  # <show> set fadeColor as color given
        self.fadeDuration = duration  # <show> set fadeDuration as duration given
        self.fadeStart = perf_counter()  # <show> set fade start as current time
        # <show> set startingPercent for ratio color as percent given
        self.startingPercent = startingPercent
        self.endingPercent = endingPercent
        # <show> find out the alpha Mutliplier so it still goes the same speed
        self.alphaMultiplier = duration/(startingPercent - endingPercent)
        self.fromfunc = False

    # <show> find the ratio between 2 different colors
    def ratioColor(self, color1, percent, fromfunc=True):
        # 1 means more color 2, which is the newer color and 0 is more color 1
        color2 = self.fadeColor.giveColorArgs()  # <show> get color2 color arguments
        multiplier = (self.startingPercent - (percent))
        if fromfunc:
            return (color1[0] - (color1[0]-color2[0])*multiplier,
                    color1[1] - (color1[1]-color2[1])*multiplier,
                    color1[2] - (color1[2]-color2[2])*multiplier,
                    color1[3] - (color1[3]-color2[3])*multiplier)  # <show> gets the ratio between the 2 different colors
        return (color2[0] + (color1[0]-color2[0])*multiplier,
                color2[1] + (color1[1]-color2[1])*multiplier,
                color2[2] + (color1[2]-color2[2])*multiplier,
                color2[3] + (color1[3]-color2[3])*multiplier)


class OverviewObject(object):
    def __init__(self):
        self.TIMEDELAY = 0
        self.PLAYERS = []  # <show> list that holds all Players
        self.TRAILS = []  # <show> list that holds all trails
        self.BULLETS = []  # <show> list that holds all Bullets
        self.BUTTONS = []
        # <show> list that holds all Player, Trails, and Bullets
        self.BULLETFADE = Fading()
        self.GLOBALFADE = Fading()
        self.PLAYERFADE = Fading()
        self.TRAILFADE = Fading()

        self.Camera = CameraObject()
        self.NEXA_BOLD = 'data/Fonts/Nexa Bold.otf'
        self.NEXA_LIGHT = 'data/Fonts/Nexa Light.otf'

        self.TOTALLIVES = 3

    def update(self):
        pass

    def clean(self):
        self.__init__()

    def quickClean(self):
        self.TRAILS = []  # <show> list that holds all trails
        self.BULLETS = []  # <show> list that holds all Bullets

# how the level script will work.
# (have an object that are bullets which get a start function on it so that they can spawn.)
# (how will I do flashes and shakes? and other game changes)
# (time)
# DICTIONARYS, basically have it so that it can be translated into
# A list of Tuples containing (when they spawn in seconds, )


Overview = OverviewObject()





def convertPointToMid(vertices):
    xCoord = [x for x, _ in vertices]
    yCoord = [y for _, y in vertices]
    xOffset, yOffset = (max(xCoord) - min(xCoord))/2 - \
        max(xCoord), (max(yCoord) - min(yCoord))/2 - max(yCoord)
    return tuple([(v[0] + xOffset, v[1] + yOffset) for v in vertices])


def cartesianToPolar(array):
    # output: tuple[tuple[int]] = []
    # for x, y in array:
    #     r: float = sqrt(x**2 + y**2)
    #     theta: float = degrees(atan2(y, x))
    #     output.append((r, theta))
    return [(sqrt(x*x + y*y), degrees(atan2(y, x))) for x, y in array]


def polarToCartesian(rAndBasetheta, angle):
    # note theta is in degrees and not radians
    # output: tuple[tuple[float]] = []
    # for i, rtheta in enumerate(rAndBasetheta):
    #     output.append((round(cos(radians(rtheta[1]+angle))*rtheta[0]),
    #                   round(sin(radians(rtheta[1]+angle))*rtheta[0])))
    # return output
    return [(cos(radians(theta+angle))*r, sin(radians(theta+angle))*r) for r, theta in rAndBasetheta]


def regularShape(radius, nSide, angleOffset=0):
    # side = side length
    if nSide < 3:
        nSide = 3  # if nSide is less that 3 it's not a shape
    offset = radians(angleOffset)
    interval = 2*pi/nSide
    return [(cos(i*interval + offset)*radius, sin(i*interval + offset)*radius) for i in range(nSide)]


def verticesForCircle(radius):
    #https://stackoverflow.com/questions/11774038/how-to-render-a-circle-with-as-few-vertices-as-possible
    return ceil(2*pi/acos(2 * (1 - 0.5 / radius)**2 - 1))

def createBox(x,y):
    return ((x, -y), (x, y), (-x, y), (-x, -y))

def RGBtoStaticColor(r=255, g=255, b=255, alpha=255):
    return {
        'r': StaticColor(r),
        'g': StaticColor(g),
        'b': StaticColor(b),
        'alpha': StaticColor(alpha)}

# https://krazydad.com/tutorials/makecolors.php
# https://www.instructables.com/How-to-Make-Proper-Rainbow-and-Random-Colors-With-/


class StaticColor(object):
    def __init__(self, color):
        self.color = color  # <show> holds the pixel color

    def returnColor(self, colorMultiplier):
        return self.color  # <show> returns pixel color


FULL_COLOR = StaticColor(255)  # <show> Holds a full Pixel Color
EMPTY_COLOR = StaticColor(0)  # <show> Holds an empty Pixel Color


class DynamicColor(object):
    def __init__(self, color, lowerBound, upperBound, overflowFunc, reverse=False):
        #what is self.color
        self.baseColor = color  # <show> holds the starting color of the color
        # <show> hold the starting and ending limits
        self.limits = (lowerBound, upperBound)
        self.difference = upperBound - lowerBound if upperBound - \
            lowerBound else 1  # <show> holds the difference between the 2 limits
        if overflowFunc != DynamicColor.modColor:
            # <show> holds the waveLength distance for sinFuncs
            self.waveLength = pi/self.difference
            # <show> holds the centre color for sinFuncs
            self.centre = (lowerBound+upperBound)/2
            # <show> is the starting angle in sinColor instead
            self.baseColor = color/360 * self.difference
        self.overflow = overflowFunc  # <show> what type of overflow Function it uses
        self.reverse = reverse  # <show> if the overflow function is reversing or not

    def returnColor(self, colorMultiplier):
        return self.overflow(self, self.baseColor + self.difference*colorMultiplier)

    def modColor(self, color):
        if self.reverse:  # <show> if overflowFunction is reversing
            # <show> if color exceeds self.limit[1] then goes to the limit[0]
            return self.limits[1] - color % self.difference
        # <show> if color goes below self.limit[0] then goes to the limit[1]
        return self.limits[0] + color % self.difference

    def sinColor(self, color):
        # <show> return the sinColor of the color as it goes between limit[0] and limit[1]
        return self.centre + sin(color*self.waveLength)*self.difference/2

    def posSinColor(self, color):
        # <show> limit[0] is now the centre and limit[1] is the peak and if it goes below it is set to 0
        return self.limits[0]+max(0, sin(color*self.waveLength)*self.difference)


class ColorOverview(object):
    def __init__(self, r=FULL_COLOR, g=FULL_COLOR, b=FULL_COLOR, alpha=FULL_COLOR, bullet=False, trail=False, player=False, isGlobal=False, starting=True, speed=1):
        # color are given a lower and upper
        self.red = r  # <show> Red Color of Color
        self.green = g  # <show> Green Color of Color
        self.blue = b  # <show> Blue Color of Color
        self.alpha = alpha  # <show> Alpha Color of Color
        if bullet:  # <show> if it is linked with a bullet
            self.fade = Fading(
                parent=(Overview.BULLETFADE, Overview.GLOBALFADE))
        elif trail:
            self.fade = Fading(
                parent=(Overview.TRAILFADE, Overview.GLOBALFADE))
        elif player:
            self.fade = Fading(
                parent=(Overview.PLAYERFADE, Overview.GLOBALFADE))
        elif isGlobal:
            self.fade = Fading(parent=(Overview.GLOBALFADE,))
        else:
            self.fade = Fading()
            # Overview.BULLETCOLORS.append(self) #<show> append it to BULLETCOLORS
        if starting:
            self.starting()
        self.speed = speed

    def update(self, dt):  # <show> if update
        pass

    def giveColorArgs(self, RGBA=True):  # <show> when giving color arguments
        # <show> color in terms of when it was created.
        ColorMultiplier = (perf_counter() - self.start)/self.speed
        if RGBA:  # <show> if alpha is wanted
            return self.fade.fading(self.red.returnColor(ColorMultiplier),
                                    self.green.returnColor(ColorMultiplier),
                                    self.blue.returnColor(ColorMultiplier),
                                    self.alpha.returnColor(ColorMultiplier))  # <show> get color of all different color base class
        return (self.red.returnColor(ColorMultiplier),
                self.green.returnColor(ColorMultiplier),
                self.blue.returnColor(ColorMultiplier))  # <show> get color of all different color base class

    def clear(self):  # <show> if color needs to be removed
        # do this and make it so it removes from COLORSPRITES
        # Overview.SPRITECOLORS.remove(self) #<show> removes color from ColorSprite List
        pass

    def copy(self):
        pass  # make it

    def starting(self):
        self.start = perf_counter()


RAINBOW = ColorOverview(
    r=DynamicColor(0, 128, 255, DynamicColor.posSinColor),
    g=DynamicColor(120, 128, 255, DynamicColor.posSinColor),
    b=DynamicColor(240, 128, 255, DynamicColor.posSinColor), isGlobal=True)  # <show> A cool Rainbow Color Object





WHITE = ColorOverview()  # <show> White Color Args


def minmax(minimum, maximum, val):
    return min(max(minimum, val), maximum)


class PolygonClass(object):  # <show> holds the polygon single shapes
    def __init__(self, vertices, color=WHITE, rotationSpeed=1, dimensions=False):
        if dimensions:
            xCoord = [x for x, _ in vertices]
            yCoord = [y for _, y in vertices]
            self.dimension = ((max(xCoord) - min(xCoord)), (max(yCoord) - min(yCoord)))
        # <show> holds the polar version of the vertices of the shape
        self.vertices = cartesianToPolar(vertices)
        self.rotationSpeed = rotationSpeed  # <show> holds the polygon rotationSpeed
        if type(color) == dict:  # <show> if color is given as a dictionary
            # <show> unpacks dictionary and is given is self.color
            self.color = ColorOverview(**color)
        else:  # <show> if it already an Object
            self.color = color  # <show> set it to self.color

    # <show> if it needs to get the cartesian coordinate of its vertices
    def giveGFXArgs(self, rotation):
        return (polarToCartesian(self.vertices, rotation*self.rotationSpeed), self.color.giveColorArgs())

    def __str__(self):
        return f'{len(self.vertices)} shape polygon with {str(self.rotation)[:5]} rotation'

class PolygonOverview(object):  # <show> Holds multiple Polygons
    def __init__(self, polygons, rotation=0, rotationIncrease=1, rotationIncreaseIncrease=0, starting=True):

        if type(polygons[0]) == dict:  # <show> if polygons are given as a dict
            self.polygons = tuple((PolygonClass(**polygon)
                                  for polygon in polygons))  # <show> unpacks polygon and create the polygons
        else:
            self.polygons = polygons  # <show> set it to Polygons
        self.internalRotation = rotation  # <show> internal Rotation is set as rotation
        # <show> rotation Increase is set as rotationIncrease
        self.internalRotationIncrease = rotationIncrease
        self.internalRotationIncreaseIncrease = rotationIncreaseIncrease
            # <show> max radius size if polar coordinate
        self.polygonSize = max(
            r for i in self.polygons for r, _ in i.vertices)
        if starting:
            self.starting()

    def update(self, dt, externalRotation=0, externalRotationIncrease=0, lives=None):  # <show> update Loop
        self.internalRotation += (externalRotationIncrease +
                                  self.internalRotationIncrease)*dt  # <show> increase internalRotation by internal and external Rotation Increase
        # <show> find the shape rotation by adding internal and external rotations
        rotation = self.internalRotation + externalRotation
        # <show> get the polygon vertices from the multiple child polygons
        self.image = drawGFXShapes([polygon.giveGFXArgs(
            rotation) for polygon in self.polygons])

    def clear(self):  # <show> if polygon needs to be removed
        # <show> remove lower polygons
        [polygon.color.clear() for polygon in self.polygons]

    def starting(self):
        [polygon.color.starting() for polygon in self.polygons]

    def fadeFrom(self, *args, **kwargs):
        [polygon.color.fade.fadeFrom(*args, **kwargs)
         for polygon in self.polygons]

    def RGBcolor(self):
        return (self.polygons[0].color.giveColorArgs(RGBA=False))
    
    def StaticDimensions(self):
        pass


# <show> drawing polygon with vertices
def drawGFXShapes(arrayOfPolygonInfo):
        # <show> draw blank Surface
    #print (arrayOfPolygonInfo)
    possibleSize = [vertex for vertices, color in arrayOfPolygonInfo for vertex in vertices]
    #print (possibleSize)
    offset = (min(possibleSize,key=itemgetter(0))[0], min(possibleSize,key=itemgetter(1))[1])
    #print (max(possibleSize,key=itemgetter(0))[0] - offset[0], max(possibleSize,key=itemgetter(1))[1] - offset[1])
    surf = pygame.Surface((max(possibleSize,key=itemgetter(0))[0] - offset[0], max(possibleSize,key=itemgetter(1))[1] - offset[1]), pygame.SRCALPHA)
    for vertices, color in arrayOfPolygonInfo:  # <show> for each polygon vertices and color
        offsetted = [(v[0]-offset[0], v[1]-offset[1])
                        for v in vertices]  # <show> offset the vertices by polygonSize

        #gfxdraw.aapolygon(surf, offsetted, color) #<show> draw the antialias part of the polygon
        # <show> dray the filled polygon
        gfxdraw.filled_polygon(surf, offsetted, color)
        # if lives is not None:
        #     gfxdraw.pie(surf, polygonSize, polygonSize, polygonSize, 0, int(2*pi/(Overview.TOTALLIVES)*lives), (0,0,0,0))
    return surf  # <show> return Surface


# <show> function that calculate the x and y vectors when given angle and velocity
def trigVectors(angle, velocity, position=(0,0), dt=1):
    rad = radians(angle)
    return (position[0] + cos(rad)*velocity*dt, position[1] + sin(rad)*velocity*dt)


class StaticPoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, dt):
        return

    def returnCoords(self):
        return (self.x, self.y)


class LinearPoint(StaticPoint):
    def __init__(self, x, y, angle, velocity):
        super().__init__(x, y)
        self.angle = angle
        self.velocity = velocity

    def update(self, dt):
        self.x, self.y = trigVectors(
            self.angle, self.velocity, (self.x, self.y), dt)


def isThereACollision(testObject1, listOfObjectBeingCollided):
    rect1 = testObject1.get_rect()  # <show> get player rect
    mask1 = testObject1.get_mask()
    for testObject2 in listOfObjectBeingCollided:  # <show> for all bullets
        rect2 = testObject2.get_rect()  # <show> get bullet rect
        if rect1.colliderect(rect2):  # <show> if bulletRect is colliding with player rect
            #print ('I see you punk')
            foo1 = testObject1.getScreenPos()
            foo2 = testObject2.getScreenPos()
            offset = (int(foo1[0] - foo2[0]), int(foo1[1] - foo2[1]))
            if testObject2.get_mask().overlap(mask1, offset):
                return True 
    return False

# (difference in time)/duration = percent so


# let's say in bullets. give a colour arg into it. it has a parent which is sprite which then has a parent which is everything.
