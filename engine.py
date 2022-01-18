from math import sin, cos, radians, sqrt, atan2
import numpy as np
from numba import jit


def cartesianToPolar(array):
    output = np.zeros_like(array)
    for i, xy in enumerate(array):
        x = xy[0]
        y = xy[1] 
        output[i][0] = sqrt(x**2 + y**2)
        output[i][1] = atan2(y, x)
    return output


@jit(nopython=True)
def polarToCartesian(rAndBasetheta, angle):
    #note theta is in degrees and not radians
    output = np.zeros_like(rAndBasetheta)
    for i, rtheta in enumerate(rAndBasetheta):
        output[i][0] = cos(radians(rtheta[1]+angle))*rtheta[0]
        output[i][1] = sin(radians(rtheta[1]+angle))*rtheta[0]
    return output