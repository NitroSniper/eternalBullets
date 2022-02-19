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
    (6.930, '''BulletObject(
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
    (6.930, '''LEVEL.loop()'''),

)