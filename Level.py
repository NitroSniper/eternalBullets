from random import random
from time import perf_counter
from Bullets import BulletObject
from enginePure import (
    regularShape,
    verticesForCircle,
    RGBtoStaticColor,
    ColorOverview,
    LinearPoint,
    PolygonOverview,
    PolygonClass
)


LEVEL0 = (
    (3, '''LEVEL.Finish(1800, 540, 0, 0)'''),
)


LEVEL1 = (
    (0, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (0.652, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (1.302, '''BulletObject(
    LinearPoint(1920, 440, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (1.732, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (2.384, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (3.461, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (4.099, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (4.765, '''BulletObject(
    LinearPoint(1920, 440, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (5.189, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (5.848, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (6.060, '''BulletObject(
    LinearPoint(1920, 140, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (6.382, '''BulletObject(
    LinearPoint(1920, 740, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (6.707, '''BulletObject(
    LinearPoint(1920, 140, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    (6.930, '''LEVEL.Finish(1800, 440, 0, 0)'''),
    (6.930, '''LEVEL.loop()'''),

)


LEVEL2 = (
    (0, '''BulletObject(
    LinearPoint(1720, 1080, 270, 5),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 4, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(20, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=5
    ),
    0.429,
    (8, PolygonOverview(
        (
            PolygonClass(regularShape(8, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ), 
        rotation=0,
        rotationIncrease=1)))'''),

    (0.429, '''Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)'''),
    (0.580, '''BulletObject(
    LinearPoint(1720, -24, 90, 5),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 4, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(20, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=5
    ),
    0.718,
    (8, PolygonOverview(
        (
            PolygonClass(regularShape(8, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ), 
        rotation=0,
        rotationIncrease=1)))'''),
    (1.298, '''Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)'''),
    (1.457, '''BulletObject(
    LinearPoint(1720, 1080, 270, 5),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 4, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(20, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=5
    ),
    0.705,
    (8, PolygonOverview(
        (
            PolygonClass(regularShape(8, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ), 
        rotation=0,
        rotationIncrease=1)))'''),
    (2.162, '''Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)'''),
    (2.312, '''BulletObject(
    LinearPoint(1720, -24, 90, 5),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 4, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(20, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=5
    ),
    0.714,
    (8, PolygonOverview(
        (
            PolygonClass(regularShape(8, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ), 
        rotation=0,
        rotationIncrease=1)))'''),
    (3.026, '''Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)'''),
    (3.185, '''BulletObject(
    LinearPoint(1720, 1080, 270, 5),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 4, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(20, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=5
    ),
    0.714,
    (8, PolygonOverview(
        (
            PolygonClass(regularShape(8, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ), 
        rotation=0,
        rotationIncrease=1)))'''),
    (3.899, '''Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)'''),
    (4.049, '''BulletObject(
    LinearPoint(1720, -24, 90, 5),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 4, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(20, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=5
    ),
    0.714,
    (8, PolygonOverview(
        (
            PolygonClass(regularShape(8, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ), 
        rotation=0,
        rotationIncrease=1)))'''),
    (4.763, '''Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)'''),
    (4.918, '''BulletObject(
    LinearPoint(1720, 1080, 270, 5),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 4, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(20, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=5
    ),
    0.714,
    (8, PolygonOverview(
        (
            PolygonClass(regularShape(8, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ), 
        rotation=0,
        rotationIncrease=1)))'''),
    (5.632, '''Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)'''),
    (5.782, '''BulletObject(
    LinearPoint(1720, -24, 90, 5),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 4, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(20, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=5
    ),
    0.714,
    (8, PolygonOverview(
        (
            PolygonClass(regularShape(8, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ), 
        rotation=0,
        rotationIncrease=1)))'''),
    (6.496, '''Overview.GLOBALFADE.fadeFrom(WHITE, 0.3, 0.1)'''),
    (6.5, '''LEVEL.Finish(1800, 440, 0, 0)'''),
    (6.925, '''LEVEL.loop()'''),
)

LEVEL3 = (
    (0, '''BulletObject(
    LinearPoint(1920, 540, 180, 3),
    PolygonOverview(
        (
            PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    6)'''),
    ((6.5, '''LEVEL.Finish(1800, 440, 0, 0)''')),
)
