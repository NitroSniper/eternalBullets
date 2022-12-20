from random import random
from time import perf_counter
from data.EngineAndSprites.Bullets import BulletObject
from data.EngineAndSprites.enginePure import (
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
    LinearPoint(1920, 645, 180, 3),
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
    LinearPoint(1920, 645, 180, 3),
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
    LinearPoint(1920, 645, 180, 3),
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
    LinearPoint(1920, 645, 180, 3),
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
    LinearPoint(1920, 645, 180, 3),
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
    LinearPoint(1920, 645, 180, 3),
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
    LinearPoint(1920, 645, 180, 3),
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
    LinearPoint(1920, 645, 180, 3),
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
    LinearPoint(1920, 225, 180, 3),
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
    LinearPoint(1920, 885, 180, 3),
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
    LinearPoint(1920, 225, 180, 3),
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
    (6.930, '''LEVEL.Finish(1800, 540, 0, 0)'''),
    (6.930, '''LEVEL.loop()'''),

)


LEVEL2 = (
    (0, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (0.580, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (1.457, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (2.312, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (3.185, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (4.049, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (4.918, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (5.782, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (6.5, '''LEVEL.Finish(1800, 540, 0, 0)'''),
    (6.925, '''LEVEL.loop()'''),
)

LEVEL3 = (
    (0, '''BulletObject(
    LinearPoint(900, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.221)'''),
    (0, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (0.385, '''BulletObject(
    LinearPoint(975, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (0.580, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (1.457, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (1.460, '''BulletObject(
    LinearPoint(1050, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),

    (2.110, '''BulletObject(
    LinearPoint(1125, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (2.312, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (2.335, '''BulletObject(
    LinearPoint(1200, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),

    (3.185, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (3.195, '''BulletObject(
    LinearPoint(1275, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),

    (3.845, '''BulletObject(
    LinearPoint(1350, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    
    (4.049, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (4.918, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (4.925, '''BulletObject(
    LinearPoint(1425, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),

    (5.760, '''BulletObject(
    LinearPoint(1500, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (5.782, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (5.910, '''BulletObject(
    LinearPoint(1575, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),

    ((6, '''LEVEL.Finish(1800, 540, 0, 0)''')),
    (6.920, '''LEVEL.loop()'''),
)

LEVEL4 = (
    (0, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (0, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.1,
    shake={'duration': 0.1, 'y': -10})'''),
    (0, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.1)'''),

        
    
    (0.1, '''BulletObject(
    LinearPoint(600, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (0.1, '''BulletObject(
    LinearPoint(1320, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),



    (0.580, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    
    
    
    (1.210, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (1.210, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),


    (1.457, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (1.860, '''BulletObject(
    LinearPoint(600, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (1.860, '''BulletObject(
    LinearPoint(1320, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),


    (2.312, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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


    (2.950, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (2.950, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),

    
    (3.185, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (3.595, '''BulletObject(
    LinearPoint(600, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (3.595, '''BulletObject(
    LinearPoint(1320, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),
    (4.049, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (4.655, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (4.655, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),    


    (4.918, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (5.3, '''BulletObject(
    LinearPoint(600, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (5.3, '''BulletObject(
    LinearPoint(1320, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),
    (5.782, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    
    (5.839, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.75,
    shake={'duration': 0.1, 'y': -10})'''),
    (5.839, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.75)'''),    
    (5.839, '''BulletObject(
    LinearPoint(960, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.75)'''),
    (6.5, '''LEVEL.Finish(1800, 540, 0, 0)'''),
    (6.948, '''LEVEL.loop()'''),
)

LEVEL5 = (
    (0, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (0, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.1,
    shake={'duration': 0.1, 'y': -10})'''),
    (0, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.1)'''),    
    (0, '''BulletObject(
    LinearPoint(960, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.1)'''),
        
    
    (0.1, '''BulletObject(
    LinearPoint(705, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (0.1, '''BulletObject(
    LinearPoint(1200, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),


    (0.290, '''BulletObject(
    LinearPoint(595, 275, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(233, verticesForCircle(233)), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    1.25,
    warning=1)'''),
    (0.36, '''BulletObject(
    LinearPoint(1325, 275, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(233, verticesForCircle(233)), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    1.25,
    warning=1)'''), 
    (0.43, '''BulletObject(
    LinearPoint(595, 815, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(233, verticesForCircle(233)), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    1.25,
    warning=1)'''),     
    (0.5, '''BulletObject(
    LinearPoint(1325, 815, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(233, verticesForCircle(233)), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    1.25,
    warning=1)'''),


    (0.580, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    
    
    
    (1.210, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (1.210, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),    
    (1.210, '''BulletObject(
    LinearPoint(960, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),
    



    (1.457, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (1.860, '''BulletObject(
    LinearPoint(705, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (1.860, '''BulletObject(
    LinearPoint(1200, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),


    (2.312, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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


    (2.950, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (2.950, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),    
    (2.950, '''BulletObject(
    LinearPoint(960, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),

    
    (3.185, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (3.595, '''BulletObject(
    LinearPoint(705, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (3.595, '''BulletObject(
    LinearPoint(1200, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),

    (3.75, '''BulletObject(
    LinearPoint(595, 275, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(233, verticesForCircle(233)), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    1.25,
    warning=1)'''),
    (3.82, '''BulletObject(
    LinearPoint(1325, 275, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(233, verticesForCircle(233)), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    1.25,
    warning=1)'''), 
    (3.89, '''BulletObject(
    LinearPoint(595, 815, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(233, verticesForCircle(233)), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    1.25,
    warning=1)'''),     
    (3.96, '''BulletObject(
    LinearPoint(1325, 815, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(233, verticesForCircle(233)), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    1.25,
    warning=1)'''),

    (4.049, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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

    (4.655, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (4.655, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),    
    (4.655, '''BulletObject(
    LinearPoint(960, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),    


    (4.918, '''BulletObject(
    LinearPoint(1680, 1080, 270, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    (5.3, '''BulletObject(
    LinearPoint(705, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5,
    shake={'duration': 0.1, 'y': -10})'''),
    (5.3, '''BulletObject(
    LinearPoint(1200, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.5)'''),
    (5.782, '''BulletObject(
    LinearPoint(1680, -24, 90, 4),
    PolygonOverview(
        (
            PolygonClass(regularShape(24, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(24, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
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
    
    (5.839, '''BulletObject(
    LinearPoint(450, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.75,
    shake={'duration': 0.1, 'y': -10})'''),
    (5.839, '''BulletObject(
    LinearPoint(1440, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.75)'''),    
    (5.839, '''BulletObject(
    LinearPoint(960, 540, 180, 0),
    PolygonOverview(
        (
            PolygonClass(createBox(20,540), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=0
    ),
    0.65,
    warning=0.75)'''),
    (6.5, '''LEVEL.Finish(1800, 540, 0, 0)'''),
    (6.922, '''LEVEL.loop()'''),
)

LEVEL6 = (
    (0, '''BulletObject(
    LinearPoint(600, 30, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    (0, '''BulletObject(
    LinearPoint(600, 90, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 150, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 210, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 270, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 330, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 390, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 450, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 510, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 570, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 630, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 690, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 750, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 810, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 870, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 930, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 990, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(600, 1050, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 30, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    (0, '''BulletObject(
    LinearPoint(1320, 90, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 150, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 210, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 270, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 330, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 390, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 450, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 510, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 570, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 630, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 690, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 750, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 810, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 870, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 930, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 990, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    
    (0, '''BulletObject(
    LinearPoint(1320, 1050, 180, 0),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    99999)'''),
    (0, '''LEVEL.Finish(1800, 540, 0, 0)'''),
)

LEVEL7 = (
    (0, '''BulletObject(
    LinearPoint(1920, 30, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    (0, '''BulletObject(
    LinearPoint(1920, 90, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 150, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 210, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 270, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 330, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 390, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 450, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 510, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 570, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 630, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 690, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 750, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 810, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 870, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 930, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 990, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (0, '''BulletObject(
    LinearPoint(1920, 1050, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),

    (3.440, '''BulletObject(
    LinearPoint(1920, 30, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    (3.440, '''BulletObject(
    LinearPoint(1920, 90, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 150, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 210, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 270, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 330, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 390, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 450, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 510, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 570, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 630, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 690, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 750, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 810, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 870, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 930, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 990, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    
    (3.440, '''BulletObject(
    LinearPoint(1920, 1050, 180, 2),
    PolygonOverview(
        (
            PolygonClass(regularShape(38, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(38, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            PolygonClass(regularShape(30, verticesForCircle(30), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
            ),
        rotation=0,
        rotationIncrease=1
    ),
    10)'''),
    (0, '''LEVEL.Finish(1800, 540, 0, 0)'''),
    (6.945, '''LEVEL.loop()''')
)