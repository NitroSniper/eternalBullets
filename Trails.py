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
        # <show> do regular creation of ScreenObjects
        super().__init__(polygon=polygon, point=point)
        # <show> add the object to the Trails List in Overview
        Overview.TRAILS.append(self)
        self.start = perf_counter()  # <show> holds the current time it was created
        self.lifeTime = lifeTime  # <show> how long the trail will survive
        self.update(0)

    def update(self, dt, externalRotation=0):
        # <show> update the polyon and position with ScreenObject.objectUpdate function
        self.objectUpdate(dt, externalRotation=externalRotation)
        if self.lifeTime < perf_counter() - self.start:  # <show> if the trail lasts longer than it's lifetime
            # <show> remove the trail from Overview.
            Overview.TRAILS.remove(self)
