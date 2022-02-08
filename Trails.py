from math import sqrt
from time import perf_counter
from enginePure import ModuleDependency, Overview
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from enginePure import PolygonOverview, PolygonClass


class TrailObject(object):
    def __init__(self, point, polygon, lifeTime):
        self.point = point
        self.polygon = polygon
        Overview.TRAILS.append(self)
        self.start = perf_counter()
        self.lifeTime = lifeTime
        self.update(0)
    def update(self, dt):
        self.polygon.update(dt)
        self.image = self.polygon.image
        self.point.update(dt)
        # print (self.polygon.polygons[0].color.giveColorArgs())
        self.x, self.y = self.point.x, self.point.y
        if self.lifeTime < perf_counter() - self.start:
            Overview.TRAILS.remove(self)
