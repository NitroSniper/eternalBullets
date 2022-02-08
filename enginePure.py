# mahie's code is not elite, i was gonna say it is but i dont like him :D



from math import sin, cos, radians, sqrt, atan2, degrees, pi, ceil, acos
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

class Overview(object):
    PLAYERS = []  # <show> list that holds all Players
    TRAILS = []  # <show> list that holds all trails
    BULLETS = []  # <show> list that holds all Bullets
    # <show> list that holds all Player, Trails, and Bullets
    SPRITES = PLAYERS + TRAILS + BULLETS
    SPRITECOLORS = []


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


def regularShape(radius, nSide):
    # side = side length
    if nSide < 3:
        nSide = 3  # if nSide is less that 3 it's not a shape
    interval = 2*pi/nSide
    return [(cos(i*interval)*radius, sin(i*interval)*radius) for i in range(nSide)]


def verticesForCircle(radius):
    # 0.5 is how much error we want
    return ceil(2*pi/acos(2 * (1 - 0.5 / radius)**2 - 1))


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
        self.difference = upperBound - lowerBound if upperBound - lowerBound else 1  # <show> holds the difference between the 2 limits
        if overflowFunc != DynamicColor.modColor:
            # <show> holds the waveLength distance for sinFuncs
            self.waveLength = 2*pi/self.difference
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
    def __init__(self, r=FULL_COLOR, g=FULL_COLOR, b=FULL_COLOR, alpha=FULL_COLOR, sprite=False):
        # color are given a lower and upper
        self.red = r #<show> Red Color of Color
        self.green = g #<show> Green Color of Color
        self.blue = b #<show> Blue Color of Color
        self.alpha = alpha #<show> Alpha Color of Color
        self.start = perf_counter() #<show> when Color was Created
        self.fadeColor = None #<show> Fade Color start
        self.fadeDuration = None #<show> Fade Color Object
        self.fadeStart = None #<show> when FadeColor was given
        self.priority = None #<show> the priority of FadeColor
        if sprite: #<show> if it is linked with a sprite
            Overview.SPRITECOLORS.append(self) #<show> add it to spriteColor list

    def update(self, dt): #<show> if update
        pass

    def giveColorArgs(self, alpha=True, fade=True): #<show> when giving color arguments
        ColorMultiplier = (perf_counter() - self.start)/1 #<show> color in terms of when it was created.
        if alpha: #<show> if alpha is wanted
            return self.fading(self.red.returnColor(ColorMultiplier),
                               self.green.returnColor(ColorMultiplier),
                               self.blue.returnColor(ColorMultiplier),
                               self.alpha.returnColor(ColorMultiplier)) #<show> get color of all different color base class
        return (self.red.returnColor(ColorMultiplier),
                self.green.returnColor(ColorMultiplier),
                self.blue.returnColor(ColorMultiplier)) #<show> get color of all different color base class

    def fading(self, r, g, b, alpha): #<show> if fading is possible
        if not self.fadeDuration:  # if fadeDuration is 0 then return
            return (r, g, b, alpha) #<show> return normal color
        elapsed = perf_counter() - self.fadeStart #<show> show the elapsed amount of time since it was created
        if elapsed/(self.alphaMultiplier) < self.startingPercent: #<show> if the fading is still happening 
            return self.ratioColor((r, g, b, alpha), elapsed/self.alphaMultiplier) #<show> return the ratio between the two colors
        else: #<show> if not fading meaning it has just finished
            self.fadeDuration = 0 #<show> set to 0
            self.priority = None #<show> it has no priority
            return (r, g, b, alpha) #<show> return normal color

    def fadeTo(self, color, duration): #<show> if fading to a Color
        pass

    def fadeFrom(self, color, duration, startingPercent=1, priority=0): #<show> if fading from a color
        if not startingPercent or bool(self.fadeDuration) and priority < self.priority:
            return
        self.fadeColor = color #<show> set fadeColor as color given
        self.fadeDuration = duration #<show> set fadeDuration as duration given
        self.fadeStart = perf_counter() #<show> set fade start as current time
        self.startingPercent = startingPercent #<show> set startingPercent for ratio color as percent given
        self.alphaMultiplier = duration/(startingPercent) #<show> find out the alpha Mutliplier so it still goes the same speed
        self.priority = priority #<show> give the fading a priority which it has

    def ratioColor(self, color1, percent): #<show> find the ratio between 2 different colors
        # 1 means more color 2, which is the newer color and 0 is more color 1
        color2 = self.fadeColor.giveColorArgs() #<show> get color2 color arguments
        return (color1[0] - (color1[0]-color2[0])*(self.startingPercent - percent),
                color1[1] - (color1[1]-color2[1])*(self.startingPercent - percent),
                color1[2] - (color1[2]-color2[2])*(self.startingPercent - percent), 
                color1[3] - (color1[3]-color2[3])*(self.startingPercent - percent)) #<show> gets the ratio between the 2 different colors

    def clear(self): #<show> if color needs to be removed
        # do this and make it so it removes from COLORSPRITES
        Overview.SPRITECOLORS.remove(self) #<show> removes color from ColorSprite List
    def copy(self):
        pass #make it


RAINBOW = ColorOverview(
    r=DynamicColor(0, 128, 255, DynamicColor.posSinColor),
    g=DynamicColor(120, 128, 255, DynamicColor.posSinColor),
    b=DynamicColor(240, 128, 255, DynamicColor.posSinColor)
) #<show> A cool Rainbow Color Object


def formaliseTupleColor(args): #<show> if Tuple is given as argument
    # tuple should look like this (func, (list of color), defualt args)
    func = args[0] #<show> function is it's first argument 
    args = [func(col, *args[2:]) for i, col in enumerate(args[1])] #<show> puts a function on args to get color args
    return ColorOverview(*args) #<show> return color args


WHITE = ColorOverview() #<show> White Color Args


class PolygonClass(object): #<show> holds the polygon single shapes
    def __init__(self, vertices, color=WHITE, rotationSpeed=1):
        self.vertices = cartesianToPolar(vertices) #<show> holds the polar version of the vertices of the shape
        self.rotationSpeed = rotationSpeed #<show> holds the polygon rotationSpeed
        if type(color) == dict: #<show> if color is given as a dictionary
            self.color = ColorOverview(**color) #<show> unpacks dictionary and is given is self.color
        elif type(color) == tuple: #<show> if it is given as a tuple
            self.color = formaliseTupleColor(color) #<show> formalise tuple to class object
        else: #<show> if it already an Object
            self.color = color #<show> set it to self.color

    def giveGFXArgs(self, rotation): #<show> if it needs to get the cartesian coordinate of its vertices
        return (polarToCartesian(self.vertices, rotation*self.rotationSpeed), self.color.giveColorArgs())

    def __str__(self):
        return f'{len(self.vertices)} shape polygon with {str(self.rotation)[:5]} rotation'


class PolygonOverview(object): #<show> Holds multiple Polygons
    def __init__(self, polygons, rotation=0, rotationIncrease=1):
        if type(polygons[0]) == dict: #<show> if polygons are given as a dict
            self.polygons = tuple((PolygonClass(**polygon)
                                  for polygon in polygons)) #<show> unpacks polygon and create the polygons
        else:
            self.polygons = polygons #<show> set it to Polygons
        self.internalRotation = rotation #<show> internal Rotation is set as rotation
        self.internalRotationIncrease = rotationIncrease #<show> rotation Increase is set as rotationIncrease
        self.polygonSize = max(r for i in self.polygons for r, _ in i.vertices) #<show> max radius size if polar coordinate

    def update(self, dt, externalRotation=0, externalRotationIncrease=0): #<show> update Loop
        self.internalRotation += (externalRotationIncrease +
                                  self.internalRotationIncrease)*dt #<show> increase internalRotation by internal and external Rotation Increase
        rotation = self.internalRotation + externalRotation #<show> find the shape rotation by adding internal and external rotations
        self.image = drawGFXShapes([polygon.giveGFXArgs(rotation) for polygon in self.polygons], self.polygonSize) #<show> get the polygon vertices from the multiple child polygons

    def clear(self): #<show> if polygon needs to be removed
        [polygon.color.clear() for polygon in self.polygons]  #<show> remove lower polygons


def drawGFXShapes(arrayOfPolygonInfo, polygonSize): #<show> drawing polygon with vertices
    surf = pygame.Surface((2*(polygonSize), 2*(polygonSize)), pygame.SRCALPHA) #<show> draw blank Surface
    for vertices, color in arrayOfPolygonInfo: #<show> for each polygon vertices and color
        offsetted = [(v[0] + polygonSize, v[1] + polygonSize)
                     for v in vertices] #<show> offset the vertices by polygonSize
        #print (offsetted, end='\r')
        gfxdraw.aapolygon(surf, offsetted, color) #<show> draw the antialias part of the polygon
        gfxdraw.filled_polygon(surf, offsetted, color) #<show> dray the filled polygon
    return surf #<show> return Surface


def trigVectors(angle, velocity, position, dt=1): #<show> function that calculate the x and y vectors when given angle and velocity
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


# (difference in time)/duration = percent so