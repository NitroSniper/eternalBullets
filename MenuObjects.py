import pygame
from enginePure import Overview
pygame.font.init()


class ScreenObject(object):
    def __init__(self, point, polygon):
        self.polygon = polygon  # <show> polygon attribute to the Object
        self.point = point  # <show> point attribute to the Object

    def objectUpdate(self, dt, externalRotation=0):
        # <show> update polygon to make new image
        self.polygon.update(dt, externalRotation)
        self.point.update(dt)  # <show> update point to find new coordinates
        self.image = self.polygon.image  # <show> image is now set to new image
        # <show> coordinate is now set to new coordinates
        self.x, self.y = self.point.x, self.point.y

    def update(self, dt, externalRotation=0):
        # <show> call self.updateObject function
        self.objectUpdate(dt, externalRotation)

    def get_rect(self):
        # <show> return the rect of the object, used in collison.
        return self.image.get_rect(topleft=(self.x, self.y))

    def get_mask(self):
        # <show> return the mask of the object, used in collision
        return pygame.mask.from_surface(self.image)


class ButtonObject(ScreenObject):
    def __init__(self, point, polygon, function, fadeColor, font=None, size=None, text=None, color=None, pos=None):
        # font, size, pos
        # <show> do regular creation of ScreenObjects
        super().__init__(polygon=polygon, point=point)
        # <show> the function that the button does when it get clicked on
        self.function = function
        # <show> the fadeColour when it is hovered over.
        self.fadeColor = fadeColor
        self.font = font  # <show> the font that the text use
        self.text = text  # <show> the text that will be displayed on the button
        self.size = size  # <show> the size of the text
        self.fontColor = color  # <show> the colour of the font
        self.fontPos = pos  # <show> the position of the font
        self.objectUpdate(0)  # <show> runs a default update on the button
        # <show> add the object button to the list of buttons.
        Overview.BUTTONS.append(self)

    def update(self, dt):
        self.objectUpdate(dt)  # <show> do regular update of point and polygon
        if self.text is not None:  # <show> if text exist to be created
            self.image.blit(pygame.font.Font(self.font, self.size).render(
                self.text, True, self.fontColor.giveColorArgs()), self.fontPos)  # <show> display the text.

    def underneathMouse(self, mousePos):
        if self.get_rect().collidepoint(mousePos):
            return True
        return False

    # def underneathMouse(self, mousePos):
    #     if self.get_rect().collidepoint(mousePos):
    #         offset = (
    #                 mousePos[0]  - self.x,
    #                 mousePos[1] - self.y
    #                 )
    #         if self.get_mask().get_at(offset):
    #             return True
    #     return False
