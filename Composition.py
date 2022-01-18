from enginePure import ModuleDependency
print (ModuleDependency.allModule)
if ModuleDependency.allModule:
    from engine import polarToCartesian, cartesianToPolar
else:
    from enginePure import polarToCartesian, cartesianToPolar
'Point Objects'







'Polygon Objects'

class PolygonOverview(object):
    def __init__(polygons)

class PolygonClass(object):
    def __init__(self, vertices):

        self.vertices = cartesianToPolar(vertices)
        self.rotation = 0
        self.rotationIncrease = 1
        self.coordinates = (200, 300)

    def update(self, dt):
        self.rotation += self.rotationIncrease*dt
        result = polarToCartesian(self.vertices, self.rotation)
    def __str__(self):
        return f'{len(self.vertices)} shape polygon with {str(self.rotation)[:5]} rotation at {self.coordinates}'