from math import sin, cos, radians, sqrt, atan2

class ModuleDependency(object):
    try:
        import numpy
        isNumpyHere = True
    except ModuleNotFoundError:
        isNumpyHere = False
    try:
        import numba
        isNumbaHere = True
    except ModuleNotFoundError:
        isNumbaHere = False
    allModule = all((isNumbaHere, isNumpyHere))
    

def cartesianToPolar(array):
    output = []
    for x, y in array:
        r = sqrt(x**2 + y**2)
        theta = atan2(y, x)
        output.append((r, theta))
    return output


def polarToCartesian(rAndBasetheta, angle):
    #note theta is in degrees and not radians
    output = []
    for i, rtheta in enumerate(rAndBasetheta):
        output.append((cos(radians(rtheta[1]+angle))*rtheta[0], 
                      sin(radians(rtheta[1]+angle))*rtheta[0]))
    return output

