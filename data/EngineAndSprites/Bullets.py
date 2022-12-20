from math import sqrt
from time import perf_counter
from data.EngineAndSprites.MenuObjects import ScreenObject
from data.EngineAndSprites.enginePure import ColorOverview, ModuleDependency, WHITE, LinearPoint, RGBtoStaticColor
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from data.EngineAndSprites.enginePure import PolygonOverview, PolygonClass
from data.EngineAndSprites.enginePure import Overview


class BulletObject(ScreenObject):
    def __init__(self, point, polygon, lifeTime, child=None, warning=0, shake=None):
        # <show> do regular creation of ScreenObjects
        super().__init__(polygon=polygon, point=point)
        self.lifeTime = lifeTime  # <show> how long the bullet last
        # <show> make the bullet fade from White
        self.hit = False
        self.polygon.fadeFrom(ColorOverview(**RGBtoStaticColor(*polygon.RGBcolor(), alpha=0)), warning, 0.8, 0.3)
        
        self.child = child
        self.warning = warning
        self.shake = shake


        self.starting()  # <show> make the bullet start




    def update(self, dt, externalRotation=0):
        self.objectUpdate(dt, externalRotation) # <show> do regular update of point and polygon    
        # <show> if the bullet has lasted longer than it's lifetime
        elapsed = perf_counter() - self.start
        if self.lifeTime < elapsed:
            if self.child is not None:  # <show> if it has a child
                Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)
                amount, polygon = self.child  # <show> get the amount of bullet and the polygon
                for i in range(amount):
                    BulletObject(
                        LinearPoint(self.point.x, self.point.y,
                                    i*360/amount, 5),
                        polygon,
                        8
                    )
            Overview.BULLETS.remove(self)  # <show> remove the Bullet
        elif self.warning > elapsed: #<show> if still in warning.
            self.hit = False #<show> can it be hit is false.
        else:
            if not self.hit:
                self.polygon.fadeFrom(WHITE, duration=1)  #<show> make it fade from white
                if self.shake is not None:
                    Overview.Camera.blinking(**self.shake)
            self.hit = True #<show> can it be hit is true.
                
    def starting(self):
        self.start = perf_counter()  # <show> get the time it was created
        self.update(0)  # <show> update itself
        Overview.BULLETS.append(self)  # <show> appends itself to BULLETS

    def __bool__(self):
        return self.hit