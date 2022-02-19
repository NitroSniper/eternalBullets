from math import sqrt
from time import perf_counter
from enginePure import ColorOverview, ModuleDependency
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from enginePure import PolygonOverview, PolygonClass
from enginePure import Overview

class BulletObject(object):


    def __init__(self, point, polygon, lifeTime):
        self.point = point
        self.polygon = polygon
        self.lifeTime = lifeTime
        self.starting()
        self.polygon.fadeFrom(ColorOverview(), duration=1)
    def update(self, dt, externalRotation=0):
        self.polygon.update(dt, externalRotation=externalRotation)
        self.image = self.polygon.image
        self.point.update(dt)
        self.x, self.y = self.point.x, self.point.y
        if self.lifeTime < perf_counter() - self.start:
            self.polygon.clear()
            Overview.BULLETS.remove(self)
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))
    
    def starting(self):
        self.start = perf_counter()
        self.update(0)
        Overview.BULLETS.append(self)
