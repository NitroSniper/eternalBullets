from math import sqrt
from time import perf_counter
from MenuObjects import ScreenObject
from enginePure import ModuleDependency
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from enginePure import PolygonOverview, PolygonClass
from enginePure import Overview

class TrailObject(ScreenObject):
    def __init__(self, point, polygon, lifeTime):
        super().__init__(polygon=polygon, point=point) #<show> do regular creation of ScreenObjects
        Overview.TRAILS.append(self)
        self.start = perf_counter()
        self.lifeTime = lifeTime
        self.update(0)
    def update(self, dt, externalRotation=0):
        self.objectUpdate(dt, externalRotation=externalRotation)
        self.image = self.polygon.image
        self.point.update(dt)
        # print (self.polygon.polygons[0].color.giveColorArgs())
        if self.lifeTime < perf_counter() - self.start:
            Overview.TRAILS.remove(self)
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))