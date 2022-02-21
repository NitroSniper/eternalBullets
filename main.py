from ctypes.wintypes import RGB
from lib2to3.pytree import convert
from msilib.schema import RadioButton
from random import randint, choice, random, randrange
from re import L
from Bullets import BulletObject
from MenuObjects import ButtonObject, ScreenObject
from Trails import TrailObject
from enginePure import EMPTY_COLOR, FULL_COLOR, WHITE, CameraObject, ColorOverview, DynamicColor, LinearPoint, PolygonClass, PolygonOverview, StaticColor, StaticPoint, convertPointToMid, regularShape, verticesForCircle, RGBtoStaticColor, RAINBOW
from math import degrees, atan2
from enginePure import Overview
import pygame
from statistics import mean
from Player import PlayerObject
from Level import LEVEL0, LEVEL1
from time import perf_counter, sleep
from pygame.locals import (
    QUIT,
    KEYDOWN,
    KEYUP,
    K_w,
    K_s,
    K_d,
    K_a,
    K_SPACE,
    K_ESCAPE
)
pygame.mixer.init()
class LevelRunner(object):
    def __init__(self, level, Music=None):
        self.level = self.convertScriptToEvalFunc(level)  #<show> converts the script into eval funcs
        self.index = 0
        print (len(self.level))
        pygame.mixer.init()
        self.ENDINGMUSIC = pygame.mixer.Sound('data/Music/EndingSound.wav')
        self.ENDINGMUSIC.set_volume(0.5)
        self.MUSIC = None
        if Music:
            self.MUSIC = pygame.mixer.Sound(f'data/Music/{Music}')
            self.MUSIC.set_volume(1)
            self.MUSIC.play(-1)
        self.start = perf_counter()
        self.Trin = None
        self.finish = None
    def update(self):
        self.spawning()
        if self.Trin is not None and self.finish is None:
            for player in Overview.PLAYERS:
                if self.Trin.get_rect().colliderect(player.get_rect()):
                    Overview.GLOBALFADE.fadeTo(WHITE, 1.6)
                    player.lastInvinciblity = perf_counter()
                    self.ENDINGMUSIC.play(1)
                    self.finish = perf_counter()
                    if self.MUSIC:
                        self.MUSIC.fadeout(1000)
        if self.finish is not None and 1.6 < perf_counter() - self.finish:
            Overview.GLOBALFADE.fadeFrom(WHITE, 1000000)
            return True
    def spawning(self):
        while self.index < len(self.level) and self.level[self.index][0] < perf_counter() - self.start:
            self.level[self.index][1]()
            self.index += 1
    def convertScriptToEvalFunc(self, level):
        return tuple([(time, eval('lambda: ' + expression)) for time, expression in level])
    def loop(self):    
        self.start = perf_counter()
        self.index = -1
    def Finish(self, *args):
        if self.Trin is None:
            self.Trin = TrailObject(
                        LinearPoint(*args),
                        PolygonOverview((PolygonClass(regularShape(40, verticesForCircle(40)), ColorOverview(
                            r=DynamicColor(0, 128, 255, DynamicColor.posSinColor),
                            g=DynamicColor(120, 128, 255, DynamicColor.posSinColor),
                            b=DynamicColor(240, 128, 255, DynamicColor.posSinColor), isGlobal=True)), PolygonClass(regularShape(38, verticesForCircle(38)), ColorOverview(alpha=EMPTY_COLOR, isGlobal=True)), PolygonClass(regularShape(30, 3), ColorOverview(**RGBtoStaticColor(r=211, g=239, b=246), isGlobal=True)), PolygonClass(regularShape(10, 3), ColorOverview(alpha=EMPTY_COLOR, isGlobal=True)),), rotationIncrease=1),
                        1000000000)


SCREEN_WIDTH = 1920 #<show> pixel Width of the game
SCREEN_HEIGHT = 1080 #<show> pixel height of the game
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_SIZE = (1280, 720) #x, y
SCREENTODISPLAYSCALAR = tuple(
        win/scr for win, scr in zip(WINDOW_SIZE, SCREEN_SIZE))
DISPLAYTOSCREENSCALAR = tuple(
    scr/win for win, scr in zip(WINDOW_SIZE, SCREEN_SIZE))
def transformMousePos(mousePos):
    return (mousePos[0]*DISPLAYTOSCREENSCALAR[0],
            mousePos[1]*DISPLAYTOSCREENSCALAR[1],)





#Window Stuff
# chad = BulletObject(
#     LinearPoint(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT), 30, 0.1),
#     PolygonOverview((PolygonClass(regularShape(120, 3), ColorOverview()), PolygonClass(regularShape(60, 3), ColorOverview(alpha=StaticColor(0))), PolygonClass(regularShape(20, 4), ColorOverview(r=FULL_COLOR, g=EMPTY_COLOR, b=EMPTY_COLOR), rotationSpeed=-1)), rotationIncrease=1),
#     1000000000)
# Overview.BULLETS = [chad]    
# test = \
# BulletObject(
#     LinearPoint(920, 140, 180, 0),
#     PolygonOverview(
#         (
#             PolygonClass(regularShape(32, 3, 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
#             PolygonClass(regularShape(32, 3, 180), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
#             PolygonClass(regularShape(25, verticesForCircle(20), 0), ColorOverview(**RGBtoStaticColor(r=255, g=57, b=112), bullet=True), rotationSpeed=1),
#             ),
#         rotation=0,
#         rotationIncrease=1
#     ),
#     200)
# test.starting()
# white = ColorOverview()
# test.polygon.fadeFrom(white, duration=1)

unit = ((LEVEL0, None), (LEVEL1, 'CorruptedPart1.wav'), None, 1)


def Game(level, Music): #<show> Call Function of the game
    pygame.mixer.init()
    Overview.clean()
    P1 = PlayerObject((K_w, K_s, K_d, K_a, K_SPACE))#<show> Object of Player 1
    global LEVEL
    LEVEL = None
    GameStart = perf_counter()
    framerates=[]
    #14, 18, 36
    Overview.BGCOLOR = ColorOverview(**RGBtoStaticColor(r=8, g=12, b=14), isGlobal=True, starting=True)
    last_dt = perf_counter()
    program_running = True #<show> Boolean that tells if the menu is running or not
    P1 = PlayerObject((K_w, K_s, K_d, K_a, K_SPACE))#<show> Object of Player 1
    Overview.PLAYERS = [P1] #<show> Holds the List of Players
    Overview.GLOBALFADE.fadeFrom(WHITE, 1)
    program_running = True
    while program_running: #<show> While Game is running
        dt = (perf_counter() - last_dt)*FPS #<show> calculate the movement multiplier for it to be time dependent
        last_dt = perf_counter() #<show> last Game Loop time
        Overview.TIMEDELAY = 0
        for event in pygame.event.get(): #<show> for new events happening
            #Start Code Block (can be simplified)
            if event.type == KEYDOWN: #if a key is pressed down
                if event.key == K_ESCAPE: #<show> if new event is quit
                    program_running = False
                for player in Overview.PLAYERS: #<show> for all players in PLAYERS
                    for direction, key in zip(player.movements, player.keys): #<show> get all directions (UP, DOWN, LEFT, RIGHT)
                        if event.key == key: #<show> if new event is player control key
                            player.movements[direction] = True #<show> set direction to True
            elif event.type == KEYUP: # if a key is pressed up
                for player in Overview.PLAYERS: #<show> for all players in PLAYERS
                    for direction, key in zip(player.movements, player.keys): #<show> get all directions (UP, DOWN, LEFT, RIGHT)
                        if event.key == key: #<show> if new event is player control key
                            player.movements[direction] = False #<show> set direction to True
            #End Code Block
            elif event.type == QUIT: #<show> if new event is quit
                program_running = False #<show> set the game loop off
        
        #GAME LOGIC


        if LEVEL is None:
            if 1 < perf_counter() - GameStart:
                LEVEL = LevelRunner(level, Music)  
        else:
            if program_running:
                program_running = not LEVEL.update()
        for player in Overview.PLAYERS: #<show> for every player
            player.update(dt) 
        for bullet in Overview.BULLETS: 
            bullet.update(dt)
        for trail in Overview.TRAILS: #<show> for every player
            trail.update(dt) #<show> update player
        Overview.Camera.update(dt)
        
        #DRAWING
        SCREEN.fill(Overview.BGCOLOR.giveColorArgs())#<show> fill the screen with the background colour
        
        for trail in Overview.TRAILS:
            SCREEN.blit(trail.image, Overview.Camera.CameraOffset(trail.x, trail.y))
        for bullet in Overview.BULLETS: #<show> for every player
            SCREEN.blit(bullet.image, Overview.Camera.CameraOffset(bullet.x, bullet.y))
        
        for player in Overview.PLAYERS: #<show> for every player
            SCREEN.blit(player.image, Overview.Camera.CameraOffset(player.x, player.y)) #<show> Paste the player image at the player coordinate on the SCREEN
        if HDMode: #<show> if High Definition Mode is True
            DISPLAY.blit(pygame.transform.smoothscale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by scaling it to it's resolution 
        else: #<show> if high Definition Mode is False
            DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by smooth scaling it to it's resolution 
        pygame.display.update() #<show> Update the Screen
        framerates.append(1/(perf_counter()-last_dt))
    print ('')
    print (f'''
Frames: {mean(framerates[10:])}
Sprites: {len(Overview.PLAYERS+Overview.BULLETS+Overview.TRAILS)}''')



def MainMenu():
    framerates=[]
    Overview.clean()

    MUSIC = pygame.mixer.Sound(f'data/Music/MenuMusic.wav')
    MUSIC.set_volume(0.3)
    MUSIC.play(-1)



    last_dt = perf_counter()
    program_running = True #<show> Boolean that tells if the menu is running or not
    ButtonObject(
        StaticPoint(1166, 259),
        PolygonOverview(
            (
                PolygonClass(((0,124), (754, 124), (754, 0), (59, 0)), ColorOverview(**RGBtoStaticColor(r=0, g=0, b=0)), rotationSpeed=1, isRotating=False),
                ),
            rotation=0,
            rotationIncrease=0
        ), Game, ColorOverview(
        r=DynamicColor(0, 26, 252, DynamicColor.sinColor),
        g=DynamicColor(0, 205, 35, DynamicColor.sinColor),
        b=DynamicColor(0, 232, 114, DynamicColor.sinColor),
    ), Overview.NEXA_BOLD, 86, 'Start', ColorOverview(**RGBtoStaticColor(r=255, g=255, b=255)), (128, 28))
    ButtonObject(
        StaticPoint(1132, 259),
        PolygonOverview(
            (
                PolygonClass(((0,124), (23, 124), (79, 0), (58, 0)), ColorOverview(
        r=DynamicColor(0, 26, 252, DynamicColor.sinColor),
        g=DynamicColor(0, 205, 35, DynamicColor.sinColor),
        b=DynamicColor(0, 232, 114, DynamicColor.sinColor),
        ), rotationSpeed=1, isRotating=False),),
        rotation=0,
        rotationIncrease=0
        ), Game, ColorOverview())

    ButtonObject(
        StaticPoint(1317, 433),
        PolygonOverview(
            (
                PolygonClass(((0, 94), (754, 94), (754, 0), (44, 0)), ColorOverview(**RGBtoStaticColor(r=0, g=0, b=0)), rotationSpeed=1, isRotating=False),
                ),
            rotation=0,
            rotationIncrease=0
        ), None, ColorOverview(**RGBtoStaticColor(r=4, g=83, b=87)), Overview.NEXA_BOLD, 64, 'Leave', ColorOverview(**RGBtoStaticColor(r=255, g=255, b=255)), (128, 20))

    ButtonObject(
        StaticPoint(1292, 433),
        PolygonOverview(
            (
                PolygonClass(((0,94), (16, 94), (60, 0), (44, 0)), ColorOverview(**RGBtoStaticColor(r=4, g=83, b=87)), rotationSpeed=1, isRotating=False),),
        rotation=0,
        rotationIncrease=0
        ), None, ColorOverview())
    
    polygonTimer = perf_counter() #<show> current time that squares are created 
    Overview.BGCOLOR = ColorOverview(**RGBtoStaticColor(r=13, g=21, b=24)) #<show> Create BackGround Colour
    shake = perf_counter() #<show> current time when square is created. 
    while program_running: #<show> While Menu is running
        dt = (perf_counter() - last_dt)*FPS #<show> calculate the movement multiplier for it to be time dependent
        last_dt = perf_counter() #<show> last Game Loop time

        mousePos = transformMousePos(pygame.mouse.get_pos()) #<show> get mouse pos
        for event in pygame.event.get(): #<show> for new events happening
            if event.type == pygame.MOUSEBUTTONDOWN: #<show> if the button is pressing down
                if event.button == 1: #<show> if it's left click
                    if currentButton is not None: #<show> 
                        function = currentButton.function #<show> get the function
                        program_running = False #<show> return
            elif event.type == KEYDOWN: #if a key is pressed down
                if event.key == K_ESCAPE: #<show> if new event is quit
                    program_running = False #<show> program sto running
            elif event.type == QUIT: #<show> if new event is quit
                program_running = False #<show> set the game loop off
        #LOGIC
        generator = iter(Overview.BUTTONS)
        currentButton = None
        Overview.Camera.update(dt) #<show> update Camera
        for button in generator: #<show> for every button
            side = next(generator) #<show> get the side button
            if any((button.underneathMouse(mousePos), side.underneathMouse(mousePos))): #<show> if the mouse is touching either of them
                button.polygon.fadeFrom(button.fadeColor, 0.5) #<show> turn to secondary Colour
                side.polygon.fadeFrom(side.fadeColor, 0.5)
                button.font = Overview.NEXA_BOLD
                currentButton = button
            else:
                button.font = Overview.NEXA_LIGHT
                
        if 0.5 < perf_counter() - polygonTimer: #<show> if it is time to create Polygon
            polygonTimer = perf_counter()
            TrailObject(LinearPoint(randint(0, 1920), 1080, 270, 1), #<show> create a square
                    PolygonOverview((PolygonClass(regularShape(randint(10, 300), 4), color=ColorOverview(
                                r=DynamicColor(0, 128, 255, DynamicColor.posSinColor),
                                g=DynamicColor(120, 128, 255, DynamicColor.posSinColor),
                                b=DynamicColor(240, 128, 255, DynamicColor.posSinColor),
                                alpha=StaticColor(80), isGlobal=True), rotationSpeed=random()*choice((-1, 1))),), randint(1,360), 1, starting=True), 7)

        if 0.46875 < perf_counter() - shake: #<show> if it is time for shake
            shake = perf_counter()
            Overview.Camera.Blinking(0.1, y=5) #<show> Screen shake
            Overview.BGCOLOR.fade.fadeFrom(WHITE, 0.1, 0.05)
        for button in Overview.BUTTONS: #<show> for all buttons 
            button.update(dt) #<show> update button
        for trail in Overview.TRAILS: #<show> for all trail in Trails
            trail.update(dt) #<show> update trail
        #Drawing
        SCREEN.fill(Overview.BGCOLOR.giveColorArgs()) #<show> fill Screen with background colour
        for trail in Overview.TRAILS:
            SCREEN.blit(trail.image, Overview.Camera.CameraOffset(trail.x, trail.y))
        
        for button in Overview.BUTTONS:
            SCREEN.blit(button.image, Overview.Camera.CameraOffset(button.x, button.y))



        if HDMode: #<show> if High Definition Mode is True
            DISPLAY.blit(pygame.transform.smoothscale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by scaling it to it's resolution 
        else: #<show> if high Definition Mode is False
            DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by smooth scaling it to it's resolution 
        pygame.display.update() #<show> Update the Screen
        framerates.append(1/(perf_counter()-last_dt))
    MUSIC.fadeout(1000)
    return function
    print ('')
    print (f'''
Frames: {mean(framerates[10:])}''')








# def Template():
#     framerates=[]
#     program_running = True #<show> Boolean that tells if the menu is running or not
#     while program_running: #<show> While Menu is running
#         dt = (perf_counter() - last_dt)*FPS #<show> calculate the movement multiplier for it to be time dependent
#         last_dt = perf_counter() #<show> last Game Loop time


        
#         for event in pygame.event.get(): #<show> for new events happening
#             if event.type == QUIT: #<show> if new event is quit
#                 program_running = False #<show> set the game loop off
#         #LOGIC 

#         #Drawing
#         if HDMode: #<show> if High Definition Mode is True
#             DISPLAY.blit(pygame.transform.smoothscale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by scaling it to it's resolution 
#         else: #<show> if high Definition Mode is False
#             DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0)) #<show> Display Screen on the Window by smooth scaling it to it's resolution 
#         pygame.display.update() #<show> Update the Screen
#         framerates.append(1/(perf_counter()-last_dt))
#     print ('')
#     print (f'''
# Frames: {mean(framerates[10:])}''')



if __name__ == '__main__':
    pygame.display.init()
    pygame.font.init()
    print ([i for i in pygame.display.list_modes() if i[0]/16 == i[1]/9])
    FPS = 120 #<show> Base Frames Per Second of the Game

    pygame.display.set_caption("Template") #<show> Sets the caption of pygame window
    #Set the Caption Window Like 'Terraria: Also Try Minecraft'
    DISPLAY = pygame.display.set_mode(WINDOW_SIZE) #True Screen
    #DISPLAY = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN) #True Screen
    SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA) #Screen to Blit on other Screen
    surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    HDMode = True #<show> whether the game runs on high definition meaning higher quality
    Music = True 


    if MainMenu():
        Game(LEVEL1, 'CorruptedPart1.wav')
        # Game (LEVEL0, None)
    pygame.display.quit()
