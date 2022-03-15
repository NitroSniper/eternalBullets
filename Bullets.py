from math import sqrt
from time import perf_counter
from MenuObjects import ScreenObject
from enginePure import ColorOverview, ModuleDependency, WHITE, LinearPoint
if ModuleDependency.allModule:
    from engine import PolygonOverview, PolygonClass
else:
    from enginePure import PolygonOverview, PolygonClass
from enginePure import Overview


class BulletObject(ScreenObject):
    def __init__(self, point, polygon, lifeTime, child=None):
        # <show> do regular creation of ScreenObjects
        super().__init__(polygon=polygon, point=point)
        self.lifeTime = lifeTime  # <show> how long the bullet last
        self.starting()  # <show> make the bullet start
        # <show> make the bullet fade from White
        self.polygon.fadeFrom(WHITE, duration=1)
        self.child = child

    def update(self, dt, externalRotation=0):
        # <show> do regular update of point and polygon
        self.objectUpdate(dt, externalRotation)
        # <show> if the bullet has lasted longer than it's lifetime
        if self.lifeTime < perf_counter() - self.start:
            if self.child is not None:  # <show> if it has a child
                amount, polygon = self.child  # <show> get the amount of bullet and the polygon
                for i in range(amount):
                    BulletObject(
                        LinearPoint(self.point.x, self.point.y,
                                    i*360/amount, 5),
                        polygon,
                        8
                    )
            self.polygon.clear()  # <show> kill the polygon
            Overview.BULLETS.remove(self)  # <show> remove the Bullet

    def starting(self):
        self.start = perf_counter()  # <show> get the time it was created
        self.update(0)  # <show> update itself
        Overview.BULLETS.append(self)  # <show> appends itself to BULLETS
