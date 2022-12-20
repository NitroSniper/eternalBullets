import pygame
from time import perf_counter
from random import randint, random
from data.EngineAndSprites.enginePure import WHITE, DecayingNumber, ModuleDependency, isThereACollision, minmax, regularShape, RAINBOW, EMPTY_COLOR, FULL_COLOR, trigVectors
from data.EngineAndSprites.Trails import TrailObject
from math import sqrt, atan2, degrees
from data.EngineAndSprites.enginePure import Overview


print(ModuleDependency.allModule)
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from data.EngineAndSprites.enginePure import PolygonOverview, PolygonClass, ColorOverview, DynamicColor, StaticPoint, StaticColor, LinearPoint, RGBtoStaticColor


class PlayerObject(object):
    DEFAULT_SPEED = 3.84

    def __init__(self, keys):
        '''DOCSTRING'''
        self.keys = keys  # <show> Player Control Key
        self.movements = {
            'UP': False,
            'DOWN': False,
            'LEFT': False,
            'RIGHT': False,
            'DASH': False,
        }  # <show> these are holding which direction the player will be moving
        self.size = 40  # <show> player size in the game
        self.x = 100  # <show> Player x coordinate
        self.y = 540  # <show> Player y coordinate
        self.speed = PlayerObject.DEFAULT_SPEED  # <show> Player movement speed
        self.vertices = 4
        self.polygon = PolygonOverview((PolygonClass(
            ((40, 40), (40, -40), (-40, -40), (-40, 40))), PolygonClass(((20, 20), (20, -20), (-20, -20), (-20, 20))),))
        polygon1 = {
            'vertices': regularShape(self.size/2, self.vertices),
            'color': {
                'r': DynamicColor(0, 2, 0, DynamicColor.sinColor),
                'g': DynamicColor(0, 97, 247, DynamicColor.sinColor),
                'b': DynamicColor(0, 199, 255, DynamicColor.sinColor),
                'player': True
            },
            'rotationSpeed': 1,
        }  # <show> polygon info argument for 1 of the polygon

        # polygon1 = {
        #     'vertices': ((80, 40), (-80, 40), (-80, -40), (80,-40)),
        #     'color': {
        #         'r': DynamicColor(0, 2, 0, DynamicColor.sinColor),
        #         'g': DynamicColor(0, 97, 247, DynamicColor.sinColor),
        #         'b': DynamicColor(0, 199, 255, DynamicColor.sinColor),
        #         'player': True
        #     },
        #     'rotationSpeed': 1,
        # }  # <show> polygon info argument for 1 of the polygon
        polygons = {
            'polygons': (polygon1,),
            'rotation': 45,
            'rotationIncrease': 0
        }  # <show> complete polygon argument
        # <show> polygon attribute to the player
        self.polygon = PolygonOverview(**polygons, starting=True)
        # self.polygon = PolygonOverview((PolygonClass(regularShape(120, 3), ColorOverview()), PolygonClass(regularShape(60, 3), ColorOverview(alpha=StaticColor(0))), PolygonClass(regularShape(20, 4), ColorOverview(r=FULL_COLOR, g=EMPTY_COLOR, b=EMPTY_COLOR), rotationSpeed=-1)))
        self.polygon.update(0)
        self.image = self.polygon.image
        self.trailSize = 8  # <show> trail size
        self.trailStart = perf_counter()  # <show> last time since trail is created
        # <show> last time since player was invincible
        self.lastInvinciblity = perf_counter()
        self.invinciblityDuration = 1
        self.dashStart = perf_counter()-1
        self.lives = 2
        self.speedMultiplier = DecayingNumber()
        self.isPressingDash = False
        self.isMoving = True
        self.lastHit = perf_counter()
    def update(self, dt, externalRotation=0):
        # <show> is Player moving? don't include last value since it is the dashing func
        self.moving = any(tuple(self.movements.values())[:-1]) and self.isMoving
        self.speedMultiplier.update()
        self.speed = PlayerObject.DEFAULT_SPEED + self.speedMultiplier.currentNumber
        direction = self.getDirection(dt)
        if self.moving:  # <show> if the player is moving
            self.x += direction[0]
            self.y += direction[1]
            if self.movements['DASH'] and 0.4 < perf_counter() - self.dashStart and not self.isPressingDash:
                for _ in range(10):
                    foo = self.createTrail((4, 8), 30, 5, 3)
                    foo.polygon.fadeFrom(WHITE, 1)
                self.polygon.fadeFrom(ColorOverview(), 0.25)
                self.dashStart = perf_counter()
                self.turnInvincible(0.15)
                self.speedMultiplier.setDecayingValue(3.84*4, 0.45)
                # self.speed = PlayerObject.DEFAULT_SPEED*6
        self.isPressingDash = self.movements['DASH']

        # if 0.125 < perf_counter() - self.dashStart:
            # self.speed = self.DEFAULT_SPEED

        # <show> add direction onto player current position

        self.x = minmax(Overview.Camera.x, 1920 +
                        Overview.Camera.x, self.x)
        self.y = minmax(Overview.Camera.y, 1080 +
                        Overview.Camera.y, self.y)

        # <show> find the angle the player is going to
        self.direction = degrees(atan2(-direction[1], -direction[0]))

        # <show> update player polygon image
        self.polygon.update(dt, externalRotation=self.direction +
                            externalRotation, lives=self.lives)
        self.image = self.polygon.image  # <show> set polygon image as image

        # <show> if moving and you can spawn another trail
        if self.moving and 0.1 < perf_counter() - self.trailStart:
            self.trailStart = perf_counter()  # <show> set trail spawn last as now
            self.createTrail((4, 12), 10, 5, 2)

        if self.invinciblityDuration < perf_counter() - self.lastInvinciblity:  # <show> if player is not invincible
            if isThereACollision(self, Overview.BULLETS):
                self.turnInvincible(1)
                self.lastHit = perf_counter()
                self.lives -= 1
                self.polygon.polygons[0].color.fade.fadeFrom(ColorOverview(
                    **RGBtoStaticColor(255, 0, 0)), duration=0.5, startingPercent=1)
                Overview.GLOBALFADE.fadeFrom(ColorOverview(
                    **RGBtoStaticColor(255, 0, 0)), duration=0.5, startingPercent=0.2)
        
        if not self.lives:
            Overview.PLAYERS.remove(self)

    def createTrail(self, size, angleVariant, rotationSpeed, velocity):
        self.trailSize = randint(*size)
        currentColor = self.polygon.polygons[0].color.giveColorArgs(
            RGBA=False)  # <show> get the current color of the player
        polygon = {
            'vertices': regularShape(self.trailSize, self.vertices),
            'color': {
                'r': StaticColor(currentColor[0]),
                'g': StaticColor(currentColor[1]),
                'b': StaticColor(currentColor[2]),
                'alpha': DynamicColor(0, 255, 0, DynamicColor.modColor, reverse=False),
                'trail': True
            }
        }  # <show> trail polygon argument
        return TrailObject(
            LinearPoint(self.x, self.y, self.direction +
                        randint(-angleVariant, angleVariant), velocity),
            PolygonOverview((polygon,), self.polygon.internalRotation, randint(1, rotationSpeed), starting=True), 1)  # <show> creating trail

    def getScreenPos(self):
        return (self.x - self.image.get_width()/2,
                self.y - self.image.get_height()/2)

    def turnInvincible(self, num):
        self.lastInvinciblity = perf_counter()
        self.invinciblityDuration = num
    
    def getDirection(self, dt):
        direction = [0,0]
        if self.movements['UP']:  # <show> if movement 'up' is True
            direction[1] -= self.speed*dt  # <show> Player moves upwards
        if self.movements['DOWN']:  # <show> if movement 'down' is True
            direction[1] += self.speed*dt  # <show> Player moves downwards
        if self.movements['LEFT']:  # <show> if movement 'left' is True
            # <show> Player moves to the left
            direction[0] -= self.speed*dt
        if self.movements['RIGHT']:  # <show> if movement 'right' is True
            # <show> Player moves to the right
            direction[0] += self.speed*dt
        return tuple(direction)

    def get_rect(self):
        # <show> return player rect
        return self.image.get_rect(center=(self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.image)


# crazy frog axel
