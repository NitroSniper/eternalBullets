from math import sqrt
from time import perf_counter
from MenuObjects import ScreenObject
from enginePure import ColorOverview, ModuleDependency, WHITE
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from enginePure import PolygonOverview, PolygonClass
from enginePure import Overview

class BulletObject(ScreenObject):
    def __init__(self, point, polygon, lifeTime):
        super().__init__(polygon=polygon, point=point) #<show> do regular creation of ScreenObjects
        self.lifeTime = lifeTime #<show> how long the bullet last
        self.starting() #<show> make the bullet start
        self.polygon.fadeFrom(WHITE, duration=1) #<show> make the bullet fade from White
    def update(self, dt, externalRotation=0):
        self.objectUpdate(dt, externalRotation) #<show> do regular update of point and polygon
        if self.lifeTime < perf_counter() - self.start: #<show> if the bullet has lasted longer than it's lifetime
            self.polygon.clear() #<show> kill the polygon
            Overview.BULLETS.remove(self) #<show> remove the Bullet
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))
    
    def starting(self):
        self.start = perf_counter() #<show> get the time it was created
        self.update(0) #<show> update itself
        Overview.BULLETS.append(self) #<show> appends itself to BULLETS
