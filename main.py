from random import randint, choice
from turtle import st
from Bullets import BulletObject
from enginePure import EMPTY_COLOR, FULL_COLOR, ColorOverview, LinearPoint, PolygonClass, PolygonOverview, StaticColor, StaticPoint, regularShape, verticesForCircle, RGBtoStaticColor, RAINBOW
from math import degrees, atan2
from enginePure import Overview
import pygame
from statistics import mean
from Player import PlayerObject
from Level import LEVEL1
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
pygame.display.init()

#


class LevelRunner(object):
    def __init__(self, level, Music=None):
        self.level = self.convertScriptToEvalFunc(level)
        self.index = 0
        print (len(self.level))
        if Music:
            pygame.mixer.init()
            MUSIC = pygame.mixer.Sound(f'Music/{Music}')
            MUSIC.set_volume(0.1)
            MUSIC.play(-1)
        self.start = perf_counter()
    def update(self):
        self.spawning()
    def spawning(self):
        while self.index < len(self.level) and self.level[self.index][0] < perf_counter() - self.start:
            self.level[self.index][1]()
            self.index += 1
    def convertScriptToEvalFunc(self, level):
        return tuple([(time, eval('lambda: ' + expression)) for time, expression in level])
    def loop(self):    
        self.start = perf_counter()
        self.index = 0







#Window Stuff
print ([i for i in pygame.display.list_modes() if i[0]/16 == i[1]/9])
FPS = 120 #<show> Base Frames Per Second of the Game
SCREEN_WIDTH = 1920 #<show> pixel Width of the game
SCREEN_HEIGHT = 1080 #<show> pixel height of the game
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_SIZE = (1920, 1080) #x, y
pygame.display.set_caption("Template") #<show> Sets the caption of pygame window
#Set the Caption Window Like 'Terraria: Also Try Minecraft'
SCREENTODISPLAYSCALAR = tuple(
    win/scr for win, scr in zip(WINDOW_SIZE, SCREEN_SIZE))
DISPLAY = pygame.display.set_mode(WINDOW_SIZE) #True Screen
#DISPLAY = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN) #True Screen
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA) #Screen to Blit on other Screen
surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
HDMode = True #<show> whether the game runs on high definition meaning higher quality
Music = True 
# chad = BulletObject(
#     LinearPoint(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT), 30, 0.1),
#     PolygonOverview((PolygonClass(regularShape(120, 3), ColorOverview()), PolygonClass(regularShape(60, 3), ColorOverview(alpha=StaticColor(0))), PolygonClass(regularShape(20, 4), ColorOverview(r=FULL_COLOR, g=EMPTY_COLOR, b=EMPTY_COLOR), rotationSpeed=-1)), rotationIncrease=1),
#     1000000000)
# Overview.BULLETS = [chad]    
P1 = PlayerObject((K_w, K_s, K_d, K_a, K_SPACE))#<show> Object of Player 1
LEVEL = LevelRunner(LEVEL1, 'CorruptedPart1.wav')
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
def Game(): #<show> Call Function of the game
    displayframe=[]
    #14, 18, 36
    Overview.BGCOLOR = ColorOverview(**RGBtoStaticColor(r=8, g=12, b=14), isGlobal=True, starting=True)
    start = 0
    #surf = pygame.Surface((100, 100)), pygame.SRCALPHA)
    Overview.PLAYERS = [P1] #<show> Holds the List of Players
    program_running = True #<show> Boolean that tells if the game is running or not
    last_dt = perf_counter() #<show> last Game Loop time
    # foo = 0
    # trin = 8
    # troll = 0
    
    flash = perf_counter()
    while program_running: #<show> While Game is running
        dt = (perf_counter() - last_dt)*FPS #<show> calculate the movement multiplier for it to be time dependent
        last_dt = perf_counter() #<show> last Game Loop time

        for event in pygame.event.get(): #<show> for new events happening
            #Start Code Block (can be simplified)
            if event.type == KEYDOWN: #if a key is pressed down
                if event.key == K_ESCAPE: #<show> if new event is quit
                    program_running = False #<show> set the game loop off
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
        LEVEL.update()
        for player in Overview.PLAYERS: #<show> for every player
            player.update(dt) 
        for bullet in Overview.BULLETS: 
            bullet.update(dt)
        for trail in Overview.TRAILS: #<show> for every player
            trail.update(dt) #<show> update player
        Overview.Camera.update(dt)

        # if 0.5 < perf_counter()-start:
        #     start = perf_counter()
        #     var = randint(-45, 45)
        #     if randint(0,1):
        #         loc = (choice((int(Overview.Camera.x), int(Overview.Camera.x + SCREEN_WIDTH))), randint(0, SCREEN_HEIGHT))
        #     else:
        #         loc = (randint(int(Overview.Camera.x), int(Overview.Camera.x + SCREEN_WIDTH)), choice((0, SCREEN_HEIGHT)))
        #     angle = degrees(atan2(P1.y-loc[1], P1.x - loc[0])) + var
        #     col = ColorOverview(**RGBtoStaticColor(r=179, g=16, b=160), bullet=True)
        #     BulletObject(
        #         LinearPoint(*loc, angle, 5),
        #         PolygonOverview((PolygonClass(regularShape(16, verticesForCircle(16)), col),),), 5)
        #     col.fade.fadeFrom(white, duration=1, startingPercent=1)
        #     Overview.TRAILFADE.fadeFrom(ColorOverview(**RGBtoStaticColor(0, 255, 0)), duration=0.1, startingPercent=1)

        # if 0.46975 < perf_counter() - flash:
        #     flash = perf_counter()
        #     Overview.Camera.Blinking(0.25, y=5)
        #     Overview.GLOBALFADE.fadeFrom(ColorOverview(**RGBtoStaticColor(255, 255, 255)), duration=0.25, startingPercent=0.1)
            #Overview.BGCOLOR.fade.fadeFrom(ColorOverview(**RGBtoStaticColor(255, 255, 255)), duration=0.25, startingPercent=0.1)
        
        # if 0 < perf_counter()-start:
        #     start = perf_counter()
        #     troll += 0.001
        #     foo += troll*dt
        #     rect = P1.get_rect()
        #     for i in range(trin):
        #         col = ColorOverview(**RGBtoStaticColor(r=179, g=16, b=160), sprite=True)
        #         BulletObject(
        #             LinearPoint(rect.center[0]-2.5, rect.center[1] - 2.5, foo+360/trin*i, 5),
        #             PolygonOverview((PolygonClass(regularShape(5, verticesForCircle(5)), col),),), 5)
        #         col.fadeFrom(white, duration=0.5, startingPercent=1, priority=1)
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
        displayframe.append(1/(perf_counter()-last_dt))
    print ('')
    print (f'''
Frames: {mean(displayframe[10:])}
Sprites: {len(Overview.PLAYERS+Overview.BULLETS+Overview.TRAILS)}''')


Game()
pygame.display.quit()
