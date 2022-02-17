from faulthandler import dump_traceback
from random import random
from time import perf_counter
class CameraObject(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        

        self.shakeOffset = (0,0)
        self.shake = (0,0)
        self.shakeDuration = 0
        self.shakeStart = 0
    def update(self, dt):
        elapsed = perf_counter() - self.shakeStart
        if not self.shakeDuration:
            pass
        elif self.shakeDuration > elapsed: #<show> means it is still going
            self.shake = self.easing(elapsed/self.shakeDuration)
        else:
            self.shake = (0,0)
            self.shakeDuration = 0

        self.x += self.dx*dt
        self.y += self.dy*dt
    def CameraOffset(self, x, y):
        return (x - (self.x + self.shake[0]), 
                y - (self.y + self.shake[1]))


    def Shaking(self, duration, magnitude):
        self.shakeDuration = duration
        self.shakeStart = perf_counter()
        self.shakeOffset = ((random()-0.5)*self.shakeMagnitude, (random()-0.5)*self.shakeMagnitude)
    
    def Blinking(self, duration, x=0, y=0):
        self.shakeDuration = duration
        self.shakeStart = perf_counter()
        self.shakeOffset = (x, y)

    def easing(self, percent): #<show> find the ratio between 2 different colors
        # 1 means more color 2, which is the newer color and 0 is more color 1
        return (self.shakeOffset[0]*(1-percent),
                self.shakeOffset[1]*(1-percent)) #<show> gets the ratio between the 2 different colors