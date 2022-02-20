import pygame
from enginePure import Overview
pygame.font.init()

class ScreenObject(object):
    def __init__(self, point, polygon):
        self.polygon = polygon #<show> polygon attribute to the Object
        self.point = point #<show> point attribute to the Object
    def objectUpdate(self, dt, externalRotation=0):
        self.polygon.update(dt, externalRotation) #<show> update polygon to make new image
        self.point.update(dt) #<show> update point to find new coordinates
        self.image = self.polygon.image #<show> image is now set to new image
        self.x, self.y = self.point.x, self.point.y #<show> coordinate is now set to new coordinates
    def update(self, dt, externalRotation=0):
        self.objectUpdate(dt, externalRotation)

    
class ButtonObject(ScreenObject):
    def __init__(self, point, polygon, function, fadeColor, font=None, size=None, text=None, color=None, pos=None):
        # font, size, pos
        super().__init__(polygon=polygon, point=point) #<show> do regular creation of ScreenObjects
        self.function = function
        self.fadeColor = fadeColor
        self.font = font
        self.text = text
        self.size = size
        self.fontColor = color
        self.fontPos = pos
        self.objectUpdate(0)
        Overview.BUTTONS.append(self)
    def update(self, dt):
        self.objectUpdate(dt) #<show> do regular update of point and polygon
        if self.text is not None:
            self.image.blit(pygame.font.Font(self.font, self.size).render(self.text, True, self.fontColor.giveColorArgs()), self.fontPos)
    def underneathMouse(self, mousePos):
        if self.get_rect().collidepoint(mousePos):
            return True
        return False
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))